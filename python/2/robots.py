import requests
import json
import sys
import re


if __name__ == '__main__':
    url = "https://www.microsoft.com"

    resp = requests.get(url)
    if resp.status_code != 200:
        sys.exit(1)

    text = ''.join(resp.text)
    p = re.compile(r'<script src=\"(.*?)\".*?>')
    for line in p.finditer(text):
        print(line.group(1))