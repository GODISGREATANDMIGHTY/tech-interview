
from collections import Counter

FILE_NAME = './python_automation_webook.txt'

with open(FILE_NAME, 'r') as f:
    for line in f:
        print(line)
        print(type(line))
    