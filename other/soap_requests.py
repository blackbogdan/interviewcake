__author__ = 'bkapusta'
import requests
from pprint import pprint
# import lxml.etree as etree
#
from xml.etree import ElementTree as ET
url = 'http://www.webservicex.com/globalweather.asmx'
# headers = "{'content-type' : 'text/xml, '}"
# headers = {'content-type' : 'text/xml', 'charset':'utf-8'}
headers = {'content-type' : 'text/xml', 'charset':'utf-8'}
body = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://www.webserviceX.NET">
   <soapenv:Header/>
   <soapenv:Body>
      <web:GetCitiesByCountry>
         <!--Optional:-->
         <web:CountryName>Ukraine</web:CountryName>
      </web:GetCitiesByCountry>
   </soapenv:Body>
</soapenv:Envelope>
'''

resp = requests.post(url, data=body, headers=headers)
text = resp.text.replace('&lt;', "<").replace("&gt;", ">")
print text
tree = ET.fromstring(text)
print tree[0][0][0][0]


