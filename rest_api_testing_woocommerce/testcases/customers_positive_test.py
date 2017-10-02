__author__ = 'bkapusta'
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
# print sys.path



from rest_api_testing_woocommerce.tools import req
from rest_api_testing_woocommerce.tools import dbconnect
from datetime import datetime
from faker import Faker
import random
import string
import json
rq = req.REQ()

def generate_random_info():
    '''

    :return:
    '''
    f = Faker()
    info = {}
    stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    info['email'] = "api_user_{}@gmail.com".format(stamp)
    info['user_name'] = "backend.{}".format(stamp)

    info['first_name'] = f.first_name()
    info['last_name'] = f.last_name()
    letters = string.lowercase
    print letters
    info['random_string'] = "".join(random.sample(letters, 8))
    return info

def test_create_customer():
    print "CREATE CUUSTOMER TEST "
    user_info = generate_random_info()
    email = user_info['email']
    user_name = user_info['email']
    fname = user_info['email']
    lname = user_info['email']
    json.dumps(user_info, indent=4)
    input_data = {
        "customer":{
            "email": email,
            "first_name": fname,
            "last_name": lname,
            "username": user_name,
            "password": "test123",
            "billing": {
                "first_name": fname,
                "last_name": lname,
                "company": "",
                "address_1": "969 Market",
                "address_2": "",
                "city": "San Francisco",
                "state": "CA",
                "postcode": "94103",
                "country": "US",
                "email": email,
                "phone": "(555) 555-5555"
            },
            "shipping": {
                "first_name": fname,
                "last_name": lname,
                "company": "",
                "address_1": "969 Market",
                "address_2": "",
                "city": "San Francisco",
                "state": "CA",
                "postcode": "94103",
                "country": "US"
    }
    }
    }
    rs = rq.post('customers', input_data)
    status_code = rs[0]
    assert status_code == 201 , "'customers' endpoint failed. status code expected: 201, Actual: {}. " \
                                "The response body is: {}, URL is: {}".format(status_code, rs[1], rs[2])

    # if call is successful then get the response body
    response_body = rs[1]['customer']
    customer_id = response_body['id']
    # print response_body
    # print customer_id

    # start verification
    assert response_body["email"] == email, "'email' in response is not as expected. " \
                                            "Expected: {exp}, Actual: {act}".format(exp=response_body["email"], act=email)

    assert response_body["username"] == user_name, "'username' in response is not as expected." \
                                                   " Expected: {exp}, Actual: {act}".format(exp=response_body["username"], act=user_name)

    assert response_body["first_name"] == fname, "'first_name' in response is not as expected." \
                                                      " Expected: {exp}, Actual: {act}".format(exp=response_body["first_name"], act=fname)

    assert response_body["last_name"] == lname, "'last_name' in response is not as expected. " \
                                                    "Expected: {exp}, Actual: {act}".format(exp=response_body["last_name"], act=lname)

    print json.dumps(rs, indent=4)

test_create_customer()


