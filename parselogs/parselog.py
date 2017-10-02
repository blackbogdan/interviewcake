__author__ = 'bkapusta'
import apachelog
import re
import sys
from pprint import pprint
import os
import paramiko
import datetime
import pandas as pd
from tabulate import tabulate

def parse_apachelog(filename):
    print "Parsing file {}".format(filename)
    headers = r'\"%{X-Forwarded-For}i\" %h \"%{bg_node}e\" %{%Y-%m-%dT%H:%M:%S}t.%{usec_frac}t%{%z}t %P \"%r\" %>s %a %b %I %D %f %O \"%{Referer}i\" \"%{User-Agent}i\" %{bg_xact_id}n %{bg_user_id}n %{bg_app_id}n \"%{bg_device_type}n\" %{bg_usage_type}n %{bg_severity}n \"%{bg_email_to}n\" \"%{bg_email_from}n\" \"%{bg_email_cc}n\" \"%{bg_email_subject}n\" \"%{bg_email_date}n\" %{bg_file_name}n %{bg_file_ext}n %{bg_keywords}n %{bg_latitude}n %{bg_longitude}n %{bg_accuracy}n \"%{bg_mime_type}n\" \"%{bg_page_title}n\" \"%{bg_field1}n\" \"%{bg_field2}n\" \"%{bg_field3}n\" \"%{bg_field4}n\" \"%{bg_field5}n\" \"%{bg_field6}n\" \"%{bg_field7}n\" \"%{bg_field8}n\" \"%{bg_field9}n\" \"%{bg_field10}n\"'
    p = apachelog.parser(headers)
    log_list = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.replace('    ', ' - - - ')
            # line = line.replace(' - -', '')
            timestamp = re.search(
                r'([0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2}T[0-9]{2,2}:[0-9]{2,2}:[0-9]{2,2}.[0-9]{1,6}\+[0-9]{1,4})', line)
            try:
                new_timestamp = '[' + timestamp.group(0) + ']'
            except AttributeError:
                print("Line '{0}' doesn't contain a timestamp. Skipping the line".format(line))
                continue
            line = line.replace(timestamp.group(0), new_timestamp)
            # print ("Parsing line {0}".format(line))
            try:
                data = p.parse(line)
            except apachelog.ApacheLogParserError:
                sys.stderr.write("Unable to parse: %s" % line)
            data['%{%Y-%m-%dT%H:%M:%S}t.%{usec_frac}t%{%z}t'] = data['%{%Y-%m-%dT%H:%M:%S}t.%{usec_frac}t%{%z}t'][
                                                                1:11] + ' ' + data['%{%Y-%m-%dT%H:%M:%S}t.%{usec_frac}t%{%z}t'][
                                                                      12:27]# + \
            #                                                     ' ' + data['%{%Y-%m-%dT%H:%M:%S}t.%{usec_frac}t%{%z}t'][
            #                                                           27:32]
            log_list.append(data)

    print "Length of currnet parsed list '{}' is: {}".format(filename, len(log_list))
    return log_list


# pprint(parse_apachelog(name_of_the_file))


def gather_files():
    # print "current folder path", os.path.dirname(os.path.abspath(__file__))
    # print os.path.abspath(__file__)
    logfiles_list = []
    z = os.walk(os.path.dirname(os.path.abspath(__file__)))
    for root, dirs, files in z:
        # print root
        # print dirs
        for filename in files:
            if filename.endswith(".log"):
                logfiles_list.append(filename)
    return logfiles_list


# print gather_files()

def get_last_3_days():
    i = 0
    list_of_filenames = []
    while i < 3:
        time = (datetime.datetime.now() - datetime.timedelta(i)).strftime("%Y.%m.%d")
        created_name = "access.{}.log".format(time)
        list_of_filenames.append(created_name)
        i += 1
    return list_of_filenames


# print get_last_3_days()


def download_logs():
    list_of_filenames = get_last_3_days()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("qac-dataplane1.us-west-2.bgcorp.com", username="ubuntu", key_filename='/Users/bkapusta/.ssh/bgcls2.pem')
    sftp = ssh.open_sftp()
    for item in list_of_filenames:
        print "Downloading {} file".format(item)
        local_path = item
        remote_path = '/opt/bg/deploy/log/{}'.format(item)
        sftp.get(remote_path, local_path)
    sftp.close()
    ssh.close()
    print "Downloaded files. Closed connection"


def remove_logs_from_folder(foldername):
    print "Removing logs"
    z = os.walk(foldername)
    for path, subfolders, files in z:
        print path, subfolders, files
        for item in files:
            if item.endswith(".log"):
                print "Removing file {}".format(os.path.join(path, item))
                os.remove(os.path.join(path,item))
# remove_logs_from_folder('/Users/bkapusta/Downloads/Chrome/interviewcake/parselogs')

def bogdans_prepare_json(raw_json):
    # creating dictionary for saving results
    result= {}
    result["response_codes_count"]= {}
    result["response_codes"]= {}
    result["bitglass_to_app"]= {}
    df = pd.DataFrame(raw_json)
    df = df.rename(columns={'%{%Y-%m-%dT%H:%M:%S}t.%{usec_frac}t%{%z}t': 'Time',
                        '%{User-Agent}i': 'User Agent',
                        '%{bg_xact_id}n': 'Transaction ID',
                        '%{bg_node}e': 'Origin',
                        '%{Referer}i': 'Real Referrer',
                        '%{bg_field2}n': 'Referrer App ID',
                        '%{bg_app_id}n': 'App ID',
                        '%{bg_user_id}n': 'User ID',
                        '%{bg_longitude}n': 'Longitude',
                        '%{bg_latitude}n': 'Latitude',
                        '%{bg_accuracy}n': 'Location Accuracy',
                        '%>s': 'Bitglass Response Code',
                        '%{bg_field6}n': 'Server Response Code',
                        '%{bg_field7}n': 'Bitglass Cookie (bgs)',
                        '%{bg_field3}n': 'Bitglass Cookie (bgk)',
                        '%{bg_severity}n': 'Severity',
                        '%{bg_keywords}n': 'Keywords',
                        '%{bg_page_title}n': 'HTML Page Title',
                        '%{bg_field8}n': 'bgfield8',
                        '%{bg_field9}n': 'bgfield9',
                        '%{bg_field10}n': 'bgfield10',
                        '%h': 'Remote Host',
                        '%b': 'Response Size',
                        '%{bg_device_type}n': 'User device type',
                        '%{bg_usage_type}n': 'Usage type',
                        '%{bg_email_to}n': 'Email header - to',
                        '%{bg_email_from}n': 'Email header - from',
                        '%{bg_email_cc}n': 'Email header - cc',
                        '%{bg_email_subject}n': 'Email header - subject',
                        '%{bg_email_date}n': 'Email header - date',
                        '%{bg_file_name}n': 'File name',
                        '%{bg_file_ext}n': 'File name extension',
                        '%{bg_mime_type}n': 'MIME type',
                        '%{bg_field1}n': 'URL',
                        '%{bg_field4}n': 'Email header - bcc',
                        '%{bg_field5}n': 'IMAP email attachment names (space-separated Base64-encoded names)',
                        '%a': 'Remote IP',
                        '%D': 'Response Time',
                        '%P': 'The process ID of the child that serviced the request',
                        '%f': 'File_Name',
                        '%I': 'Request Size',
                        '%O': 'Bytes Sent',
                        '%r': 'Request',
                        '%{X-Forwarded-For}i': 'IP Address'}
    )
    #We are not going to use all the data, so let's delete some of the columns:
    del df['MIME type']
    del df['Origin']
    del df['HTML Page Title']
    del df['Severity']
    del df['User device type']
    del df['Referrer App ID']
    del df['Bitglass Cookie (bgk)']
    del df['IMAP email attachment names (space-separated Base64-encoded names)']
    del df['Latitude']
    del df['Longitude']
    del df['Usage type']
    del df['Bitglass Cookie (bgs)']
    del df['File name extension']
    del df['File name']
    del df['Request']
    del df['File_Name']
    del df['Keywords']
    del df['Email header - bcc']
    del df['Email header - cc']
    del df['Email header - date']
    del df['Email header - from']
    del df['Email header - subject']
    del df['Email header - to']
    del df['bgfield8']
    del df['bgfield9']
    del df['bgfield10']
    #Convert Time column to datetime format and make an index out of it (pop will drop original Time column):
   # print "Time before indexing: ", df
   #  print "DF before,", df.head(5)
    print tabulate(df.head(5), headers='keys', tablefmt='psql')
    print "="*30

    # print pd.to_datetime(df.pop('Time'), utc=True, errors='ignore')
    # print df.set_index()
    df.index = pd.to_datetime(df.pop('Time'), utc=True, errors='ignore')
    print "df after indexing: ", df.head()

     #The Status variable is a string type, so we have to change it to int:
    df['Bitglass Response Code'] = df['Bitglass Response Code'].astype('int')

    #getting rid of users who don't belong to the company. Creating new DataFrame with only specific users to the
    # company
    # df_cleared= df[df['User ID'].isin(users_list)]
    # #reset index to access the Time column
    df= df.reset_index()
    result["response_codes_count"]["server4xx"] = df[(df['Server Response Code'] >= "400")
                                                                    & (df['Server Response Code'] < "500")].to_json(orient="records")
    #
    result["response_codes_count"]["server5xx"] = df[(df['Server Response Code'] >= "500")
                                                                    & (df['Server Response Code'] < "600")].to_json(orient="records")
    result["response_codes_count"]["bitglass5xx"] = df[(df['Bitglass Response Code'] >= 400)
                                                                    & (df['Bitglass Response Code'] < 500)].to_json(orient="records")
    #
    return result

def prepare_json(json_obj, users_list=None):

    # logger.info("Start parsing json object", also_console=True)
    result= {}
    result["response_codes_count"]= {}
    result["response_codes"]= {}
    result["bitglass_to_app"]= {}
    df = pd.DataFrame(json_obj)
    df = df.rename(columns={'%{%Y-%m-%dT%H:%M:%S}t.%{usec_frac}t%{%z}t': 'Time',
                            '%{User-Agent}i': 'User Agent',
                            '%{bg_xact_id}n': 'Transaction ID',
                            '%{bg_node}e': 'Origin',
                            '%{Referer}i': 'Real Referrer',
                            '%{bg_field2}n': 'Referrer App ID',
                            '%{bg_app_id}n': 'App ID',
                            '%{bg_user_id}n': 'User ID',
                            '%{bg_longitude}n': 'Longitude',
                            '%{bg_latitude}n': 'Latitude',
                            '%{bg_accuracy}n': 'Location Accuracy',
                            '%>s': 'Bitglass Response Code',
                            '%{bg_field6}n': 'Server Response Code',
                            '%{bg_field7}n': 'Bitglass Cookie (bgs)',
                            '%{bg_field3}n': 'Bitglass Cookie (bgk)',
                            '%{bg_severity}n': 'Severity',
                            '%{bg_keywords}n': 'Keywords',
                            '%{bg_page_title}n': 'HTML Page Title',
                            '%{bg_field8}n': 'bgfield8',
                            '%{bg_field9}n': 'bgfield9',
                            '%{bg_field10}n': 'bgfield10',
                            '%h': 'Remote Host',
                            '%b': 'Response Size',
                            '%{bg_device_type}n': 'User device type',
                            '%{bg_usage_type}n': 'Usage type',
                            '%{bg_email_to}n': 'Email header - to',
                            '%{bg_email_from}n': 'Email header - from',
                            '%{bg_email_cc}n': 'Email header - cc',
                            '%{bg_email_subject}n': 'Email header - subject',
                            '%{bg_email_date}n': 'Email header - date',
                            '%{bg_file_name}n': 'File name',
                            '%{bg_file_ext}n': 'File name extension',
                            '%{bg_mime_type}n': 'MIME type',
                            '%{bg_field1}n': 'URL',
                            '%{bg_field4}n': 'Email header - bcc',
                            '%{bg_field5}n': 'IMAP email attachment names (space-separated Base64-encoded names)',
                            '%a': 'Remote IP',
                            '%D': 'Response Time',
                            '%P': 'The process ID of the child that serviced the request',
                            '%f': 'File_Name',
                            '%I': 'Request Size',
                            '%O': 'Bytes Sent',
                            '%r': 'Request',
                            '%{X-Forwarded-For}i': 'IP Address'})

    #We are not going to use all the data, so let's delete some of the columns:

    del df['MIME type']
    del df['Origin']
    del df['HTML Page Title']
    del df['Severity']
    del df['User device type']
    del df['Referrer App ID']
    del df['Bitglass Cookie (bgk)']
    del df['IMAP email attachment names (space-separated Base64-encoded names)']
    del df['Latitude']
    del df['Longitude']
    del df['Usage type']
    del df['Bitglass Cookie (bgs)']
    del df['File name extension']
    del df['File name']
    del df['Request']
    del df['File_Name']
    del df['Keywords']
    del df['Email header - bcc']
    del df['Email header - cc']
    del df['Email header - date']
    del df['Email header - from']
    del df['Email header - subject']
    del df['Email header - to']
    del df['bgfield8']
    del df['bgfield9']
    del df['bgfield10']


    #Convert Time column to datetime format and make an index out of it (pop will drop original Time column):
   # print "Time before indexing: ", df
    df.index = pd.to_datetime(df.pop('Time'), utc=True)
    # df["Time2"] = pd.to_datetime(df['Time'])
    print "df after indexing: ", df

    #The Status variable is a string type, so we have to change it to int:
    df['Bitglass Response Code'] = df['Bitglass Response Code'].astype('int')

    #getting rid of users who don't belong to the company
    df_cleared= df[df['User ID'].isin(users_list)]
    # #print "here is df: ", df
    #
    # #reset index to access the Time column
    # df_cleared = df_cleared.reset_index()
    # result["response_codes_count"]["server4xx"] = df_cleared[(df_cleared['Server Response Code'] >= "400")
    #                                                                 & (df_cleared['Server Response Code'] < "500")].to_json(orient="records")
    #
    # result["response_codes_count"]["server5xx"] = df_cleared[(df_cleared['Server Response Code'] >= "500")
    #                                                                 & (df_cleared['Server Response Code'] < "600")].to_json(orient="records")
    # result["response_codes_count"]["bitglass5xx"] = df_cleared[(df_cleared['Bitglass Response Code'] >= 400)
    #                                                                 & (df_cleared['Bitglass Response Code'] < 500)].to_json(orient="records")

    # return result

def parse_several_apaches_and_return_list():
    # download_logs()
    list_with_log_names = gather_files()
    combined_logs = []
    for item in list_with_log_names:
        combined_logs.extend(parse_apachelog(item))

    print "Final length of combined logs", len(combined_logs)
    print combined_logs[0]
    # prepare_json(combined_logs)
    its_the_final_result = bogdans_prepare_json(combined_logs)
    return its_the_final_result

import json
with open("parsing_result.json", "w") as f:
    x = parse_several_apaches_and_return_list()
    f.write(json.dumps(x, indent=4))













# def bg_parse_apache_log_files(file_name, logformats=[".log"]):
#     nformat = r'\"%{X-Forwarded-For}i\" %h \"%{bg_node}e\" %{%Y-%m-%dT%H:%M:%S}t.%{usec_frac}t%{%z}t %P \"%r\" %>s %a %b %I %D %f %O \"%{Referer}i\" \"%{User-Agent}i\" %{bg_xact_id}n %{bg_user_id}n %{bg_app_id}n \"%{bg_device_type}n\" %{bg_usage_type}n %{bg_severity}n \"%{bg_email_to}n\" \"%{bg_email_from}n\" \"%{bg_email_cc}n\" \"%{bg_email_subject}n\" \"%{bg_email_date}n\" %{bg_file_name}n %{bg_file_ext}n %{bg_keywords}n %{bg_latitude}n %{bg_longitude}n %{bg_accuracy}n \"%{bg_mime_type}n\" \"%{bg_page_title}n\" \"%{bg_field1}n\" \"%{bg_field2}n\" \"%{bg_field3}n\" \"%{bg_field4}n\" \"%{bg_field5}n\" \"%{bg_field6}n\" \"%{bg_field7}n\" \"%{bg_field8}n\" \"%{bg_field9}n\" \"%{bg_field10}n\"'
#     p = apachelog.parser(nformat)
#     log_list = []
#     def parse_log_lines(file_name):
#         with open(file_name) as f:
#             for line in f.readlines():
#                 # print "Raw line before any changes :", line
#                 #surround a server time in square brackets to prevent error: Unable to parse apachelog
#                 line = line.replace('    ', ' - - - ')
#                 #print "line after any 1st change :", line
#                 timestamp = re.search('([0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2}T[0-9]{2,2}:[0-9]{2,2}:[0-9]{2,2}.[0-9]{1,6}\+[0-9]{1,4})', line)
#                 #print 'timestamp:', timestamp.group(0)
#                 try:
#                     new_timestamp = '[' + timestamp.group(0) + ']'
#                 except AttributeError:
#                     print("Line '{0}' doesn't contain a timestamp. Skipping the line".format(line))
#                     continue
#                 line = line.replace(timestamp.group(0), new_timestamp)
#                 # print ("Parsing line {0}".format(line))
#                 try:
#                     data = p.parse(line)
#                 except apachelog.ApacheLogParserError:
#                     sys.stderr.write("Unable to parse %s" % line)
#                     print
#                 data['%{%Y-%m-%dT%H:%M:%S}t.%{usec_frac}t%{%z}t'] = data['%{%Y-%m-%dT%H:%M:%S}t.%{usec_frac}t%{%z}t'][1:11]+ \
#                                                                     ' '+data['%{%Y-%m-%dT%H:%M:%S}t.%{usec_frac}t%{%z}t'][12:27]+ \
#                                                                     ' '+data['%{%Y-%m-%dT%H:%M:%S}t.%{usec_frac}t%{%z}t'][27:32]
#                 log_list.append(data)
#                 # print("Got parsed lines from the line: {0}".format(data), also_console=True)
#     parse_log_lines(file_name)
#     Now let's parse each line while preparing the access time so that pandas will be able to handle it.
#     for root, dirs, files in os.walk(folder):
#         print root, dirs, files
#         for file in files:
#             print "going to parse file {0}".format(file)
#             print("Going to parse file {0}".format(file), also_console=True)
#             extension = os.path.splitext(file)[1]
#             if extension not in logformats:
#                 print("File {0} has extension {1}, which is not listed in logformats to check: {2}. "
#                             "Skipping the file".format(file, extension, logformats), also_console=True)
#                 continue
#
#             parse_log_lines(os.path.join(root, file))
#             print("Finished parsing file {0}".format(file), also_console=True)
#          sample_string = '"10.1.0.20" 10.70.0.215 "qac-dataplane2.us-west2" [2016-01-04T03:31:00.053108+0000] 4945 "GET /images/cleardot.gif?zx=v7f3rjm3oi12 HTTP/1.1" 200 10.70.0.215 43 2431 330765 proxy:https://www.google.com/images/cleardot.gif?zx=v7f3rjm3oi12 6722 "https://1.client-channel.google.com/client-channel/client?cfg=%7B%222%22%3A%22cello%22%2C%224%22%3A%22appscommonstorage%22%2C%228%22%3Afalse%2C%2213%22%3Afalse%7D&ctype=cello&service=appscommonstorage&xpc=%7B%22cn%22%3A%220Cu8BCPPPO%22%2C%22tp%22%3Anull%2C%22osh%22%3Anull%2C%22ppu%22%3A%22https%3A%2F%2Fdrive.google.com%2Frobots.txt%22%2C%22lpu%22%3A%22https%3A%2F%2F1.client-channel.google.com%2Frobots.txt%22%7D" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36" VonndApGCv0AABNR5HwAAAGM - 1 "-" - - "-" "-" "-" "-" "-" - - - - - - "-" "-" "https://www.google.com/images/cleardot.gif?zx=v7f3rjm3oi12" "-" "-" "-" "-" "200" "-" "-" "-" "-"'
#     print("Finished parsing directory {0}. Result list has length {1}".format(folder, len(log_list)), also_console=True)
#     return log_list

# print bg_parse_apache_log_files(name_of_the_file)
