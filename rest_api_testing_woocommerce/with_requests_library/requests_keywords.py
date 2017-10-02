__author__ = 'bkapusta'
from woocommerce import API
class REQ:
    def return_object(self):

        admin_consumer_key = 'ck_d46283593b62ed3b10e12f646fdc2afccb672575'
        admin_consumer_secret = 'cs_cafbc6686cc0f0a6d1a4a34c2d90ddfda8811822'

        self.wcapi = API(
            url = 'http://127.0.0.1/bkstore',
            consumer_key=admin_consumer_key,
            consumer_secret=admin_consumer_secret,
            version="v3"
        )
        return self.wcapi


req = REQ()
z = req.return_object()
print z.consumer_key
print type(z)
