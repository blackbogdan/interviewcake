__author__ = 'bkapusta'
import requests
def authenticate(username = "ruslan@gmail.com", password = "SpaceMan"):
    base_url = 'https://www.instagram.com'
    s = requests.session()
    bogdan_headers = {'user-agent':'Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}
    s.get(base_url, headers = bogdan_headers)

    # csrf token is stored in cookies you can have a look here. Why?
    # because fo the line "s = requests.session()". We establish the session, so it keeps cookies
    # print s.cookies.get_dict()

    body = {'username':'{}'.format(username),
            'password':'{}'.format(password)}
    login_headers = {
        'x-csrftoken': '{}'.format(s.cookies.get_dict()['csrftoken']),
        'x-instagram-ajax': '1',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
        'accept': '*/*',
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://www.instagram.com/'
    }
    login_response = s.post('{}/accounts/login/ajax/'.format(base_url), headers=login_headers, data=body)
    print login_response.status_code
    print login_response.headers
    print login_response.text

    # just in case you want to write response to file and open it in browser
    # with open("instagram.html", "w") as f:
    #     f.write(login_response.text)
authenticate()
