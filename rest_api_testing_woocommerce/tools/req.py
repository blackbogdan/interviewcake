__author__ = 'bkapusta'
from woocommerce import API

class REQ():
    def __init__(self):
        admin_consumer_key = 'ck_d46283593b62ed3b10e12f646fdc2afccb672575'
        admin_consumer_secret = 'cs_cafbc6686cc0f0a6d1a4a34c2d90ddfda8811822'

        self.wcapi = API(
            url = 'http://127.0.0.1/bkstore',
            consumer_key=admin_consumer_key,
            consumer_secret=admin_consumer_secret,
            version="v3"
        )

    def test_api(self):
        '''

        :return:
        '''
        print self.wcapi.get("").json()
        print self.wcapi.get("").status_code

    def post(self, endpoint, data):
        '''

        :param endpoint:
        :param data:
        :return:
        '''
        result = self.wcapi.post(endpoint, data)
        rs_code = result.status_code
        rs_body = result.json()
        rs_url = result.url

        return [rs_code, rs_body, rs_url]

    def get(self, endpoint):
        '''

        :param endpoint:
        :return:
        '''
        result = self.wcapi.get(endpoint)
        rs_code = result.status_code
        rs_body = result.json()
        rs_url = result.url

        return [rs_code, rs_body, rs_url]