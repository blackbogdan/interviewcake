__author__ = 'bkapusta'
from Selenium2Library import Selenium2Library
import requests
import json
from robot.api import logger
from pprint import pprint

from faker import Faker
'''executing soql with REST in sf:
Status codes:
https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/errorcodes.htm
Salesforce's apis
https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/dome_update_fields.htm
rest api sf authentication:
https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_username_password_oauth_flow.htm
IMPORTANT: You MUST use python that has latest openssl library.
How to change python interpreter
https://www.jetbrains.com/help/pycharm/2017.1/configuring-available-python-interpreters.html
'''

class REST_salesforce():
    def sf_rest_authenticate(self):
        oauth_url = 'https://login.salesforce.com/services/oauth2/token'
        grant_type = 'password'
        username = '1bogdankapusta@gmail.com'
        password = 'Swordf1sh'
        consumer_key = '3MVG9CEn_O3jvv0xDqg0oQPw4zwEryYECFvQNHzjlyuw9Bv_qZnT7_UfX9dzdTCYeCKFWJMfYnIeXFpA3Hw6l'
        consumer_secret = '5456867706928955542'
        security_token = "z5VURK58ZXNRr6QbZrfFCVXv"
        s = requests.session()

        # headers = {'content-type' : 'application/json', 'charset':'utf-8'}
        headers = {'content-type' : 'application/x-www-form-urlencoded'}
        # headers = {'content-type' : 'text/xml', 'charset':'utf-8'}
        body = {
            'grant_type':grant_type,
            'username':username,
            'password':password+security_token,
            'client_id':consumer_key,
            'client_secret':consumer_secret
        }

        resp = s.post(oauth_url, data=body, headers=headers)
        # pprint(resp.json())
        d = json.loads(resp.text)
        return d

    def query_sf_rest_with_python(self, search_string="RobotProject*"):
        search_string = search_string.replace("*", "")
        logger.info(search_string, also_console=True)
        s = self.sf_rest_authenticate()

        pprint(s)
        headers = {"Authorization":"Bearer %s" %(s['access_token'])}
        query = "Select Name, Phone, Account.Name, Owner.Alias, Email from" \
                " Contact where Name LIKE '%{}%'".\
            replace(" ", "+").\
            format(search_string)
        print "....", query
        logger.info(query, also_console=True)
        query.replace("*", "")
        logger.info("=============>", also_console=True)
        logger.info(query, also_console=True)

        # print query
        # print get_columns_from_select_statement(query)
        # print "lllllllll>>>>>>", z.f(query)
        url = "%s/services/data/v39.0/query/?q=%s" %(s['instance_url'], query)
        print ">>>>>", url
        resp = requests.get(url, headers=headers)
        if resp.status_code!=200:
            raise ValueError("Stopped execution, got response status coode: %s. "\
                             "Please verify specified query" %resp.status_code)
        pprint(resp.status_code)
        records_list = resp.json()["records"]
        # pprint(records_list)
        for record in records_list:
            del record['attributes']
            record["Owner"]=record["Owner"]["Alias"]
            if record["Account"]==None:
                record["Account"] = " "
            record["Account Name"]=record.pop("Account")
            record["Contact Owner Alias"]=record.pop("Owner")
        records_list.sort(key=lambda x: x['Name'])
        # to fail uncomment this next line:
        # records_list.sort(key=lambda x: x['Name'], reverse=True)
        logger.info(json.dumps(records_list, indent=4), also_console=True, html=True)
        return records_list

    def create_account(self, acc_name=None):
        s = self.sf_rest_authenticate()
        pprint(s)
        url = 'https://na50.salesforce.com/services/data/v39.0/sobjects/Account/'
        headers = {"Authorization":"Bearer %s" %(s['access_token']),
                   "Content-Type": "application/json"}
        # body = json.loads('{\"Name\":\"Squirrel Star\"}')
        body = {"Name":"Squirrel asdfasdf"}
        print "body is: ", body
        response = requests.post(url, json=body, headers=headers)
        print "WHat I have created?"
        pprint(response.text)
        pprint(response.status_code)
        # pprint(response.headers)

    def update_account(self, record_id):
        # curl https://***yourInstance***.salesforce.com/services/data/v20.0/sobjects/Account/001D000000INjVe
        # -H "Authorization: Bearer token" -H "Content-Type: application/json" -d @patchaccount.json -X PATCH
        s = self.sf_rest_authenticate()
        url = 'https://na50.salesforce.com/services/data/v39.0/sobjects/Account/{}'.format(record_id)
        headers = {"Authorization":"Bearer %s" %(s['access_token']),
                   "Content-Type": "application/json"}
        street = Faker().military_ship()
        city = Faker().city()
        body = {"BillingStreet":street,
                "BillingCity":city  }
        resp = requests.patch(url, headers=headers, json=body)
        return resp

    def delete_record(self, record_id):
        # curl https://***yourInstance***.salesforce.com/services/data/v20.0/sobjects/Account/001D000000INjVe -H "Authorization: Bearer token" -X DELETE
        s = self.sf_rest_authenticate()
        url = 'https://na50.salesforce.com/services/data/v39.0/sobjects/Account/{}'.format(record_id)
        headers = {"Authorization":"Bearer %s" %(s['access_token'])}
        resp = requests.delete(url, headers=headers)
        return resp

    def request_head(self, record_id):
        s = self.sf_rest_authenticate()
        url = 'https://na50.salesforce.com/services/data/v39.0/sobjects/Account/{}'.format(record_id)
        headers = {"Authorization":"Bearer %s" %(s['access_token'])}
        resp = requests.head(url, headers=headers)
        resp = requests.get(url, headers=headers)
        return resp

    def request_options(self):
        s = self.sf_rest_authenticate()
        url = 'https://na50.salesforce.com/services/data/v39.0/sobjects/Account/0016A000003MZjC'
        resp = requests.options(url)
        return resp

if __name__=="__main__":
    sf_rest = REST_salesforce()
    # m = sf_rest.query_sf_rest_with_python()
    # m = sf_rest.create_account()
    # print sf_rest.update_account("0016A000003MZjM").status_code
    # print sf_rest.update_account("0016A000003MZjM").headers
    #

    # delete_resp = sf_rest.delete_record("0016A000003MZjM")
    # pprint(delete_resp)
    # pprint(delete_resp.status_code)
    # pprint(delete_resp.text)
    z = sf_rest.request_options()
    print z.json()
    print z.text
    print z.headers


    # pprint(sf_rest.request_head("0016A000003MZjC").status_code)
    # pprint(sf_rest.request_head("0016A000003MZjC").text)
