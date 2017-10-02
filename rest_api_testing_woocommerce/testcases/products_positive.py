import sys
import os
# from ..tools import req this will fail with error
#     from ..tools import req
# ValueError: Attempted relative import in non-package
from rest_api_testing_woocommerce.tools import req
from rest_api_testing_woocommerce.tools import dbconnect
from pprint import pprint
import json
rq = req.REQ()
qry = dbconnect.DBConnect()
def create_a_product():
    '''

    :return:
    '''
    global product_id
    global title
    global price
    title = 'TEST1 TITLE'
    price = '92.99'
    input_data = {
        'product':{
            'title':title,
            'type':'simple',
            'regular_price': price}
        }
    info = rq.post('products', input_data)
    # pprint(info)

    # look at our post function: it returns return [rs_code, rs_body, rs_url]
    response_code = info[0]
    response_body = info[1]
    # print json.dumps(response_body, indent=4)
    assert response_code==201, "Status code is not equal to 201."
    rs_title = response_body['product']['title']
    rs_price = response_body['product']['regular_price']
    product_id = response_body['product']['id']
    assert rs_title == title, "Response titel is not equal to entered: {}. Actual: {}".format(title, rs_title)
    assert str(rs_price) == str(price), "Response price is not equal to entered: {} Actual : {}".format(price, rs_price)
    print "test Pass"
    # print json.dumps(info, indent=4)


def test_verify_product_created_in_db():
    '''

    :return:
    '''
#      get info from db
    print product_id
    sql = '''SELECT p.post_title, p.post_type, pm.meta_value FROM bk_posts p JOIN bk_postmeta pm ON p.id=pm.post_id WHERE p.id ={} AND pm.meta_key='_regular_price' '''.format(product_id)
    qrs = qry.select('wp904', sql)
    print qrs
        # extracting the data
    db_title = qrs[0][0]
    db_type = qrs[0][1]
    db_regular_price = qrs[0][2]

    print "Verifying the product title"
    assert db_title == title, "The tile in db is not as expected. DB title: {}, Expected: {}".format(db_title, title)

    print "Verifying the post_type"
    assert db_type == 'product', "The post_type in DB is not 'product'. Expected: 'product', Actual: {}".format(db_type)

    print "Verifying the product regular price"
    assert db_regular_price == price, "The regular price in db is not as expected. Expected: {}, Actual: {}".format(price, db_regular_price)

    print "'products positive tc, verify product created in db, PASS"

create_a_product()
test_verify_product_created_in_db()