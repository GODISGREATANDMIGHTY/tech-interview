
import requests

def main():
    url = 'https://jsonplaceholder.typicode.com/users'

    resp = None
    try:
        resp = requests.get(url)
        if resp.status_code != 200:
            return
    except:
        print("error")

    if resp is None:
        return

    users = resp.json()

    for user in users:
        print(user['name'])
    

if __name__ == '__main__':
    main()