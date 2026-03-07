File Exists

import os
print(os.path.exists("sample.txt"))
----------------------------------------------
Delete File

os.remove("sample.txt")
----------------------------------------------
Copy File

import shutil
shutil.copy("source.txt", "destination.txt")
----------------------------------------------
List Files in Directory

print(os.listdir("."))
----------------------------------------------
Replace String

s = "Hello World"
print(s.replace("World", "Python"))
----------------------------------------------
String Formatting

name = "Alice"
age = 25
print(f"{name} is {age} years old")
----------------------------------------------
Count Substring

s = "banana"
print(s.count("a"))
----------------------------------------------
Reverse String

s = "Python"
print(s[::-1])
----------------------------------------------
Rename Files in Directory

import os
for filename in os.listdir("."):
    if filename.endswith(".txt"):
        os.rename(filename, filename.upper())
----------------------------------------------
Download File from URL

import requests
url = "https://example.com/file.txt"
r = requests.get(url)
with open("file.txt", "wb") as f:
    f.write(r.content)
----------------------------------------------
Run Shell Command

import subprocess
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)
----------------------------------------------
Monitor Folder for New Files

import time, os
folder = "."
existing = set(os.listdir(folder))
while True:
    time.sleep(5)
    new = set(os.listdir(folder)) - existing
    if new:
        print("New files:", new)
        existing.update(new)
----------------------------------------------
import os, shutil, glob

# 1. List all files in directory
files = os.listdir(".")
print(files)

# 2. List all .txt files
txt_files = glob.glob("*.txt")
print(txt_files)

# 3. Rename all .txt files to uppercase
for f in txt_files:
    os.rename(f, f.upper())

# 4. Move all .jpg files to 'images/' folder
os.makedirs("images", exist_ok=True)
for f in glob.glob("*.jpg"):
    shutil.move(f, "images/" + f)

# 5. Delete all .log files
for f in glob.glob("*.log"):
    os.remove(f)

# 6. Copy all .csv files to backup folder
os.makedirs("backup", exist_ok=True)
for f in glob.glob("*.csv"):
    shutil.copy(f, "backup/" + f)

# 7. Count number of lines in all .txt files
for f in txt_files:
    with open(f) as file:
        print(f, len(file.readlines()))

# 8. Read first line of each file
for f in txt_files:
    with open(f) as file:
        print(f, file.readline())

# 9. Append text to all .txt files
for f in txt_files:
    with open(f, "a") as file:
        file.write("\nAppended by script")

# 10. Rename files by adding timestamp
import time
for f in txt_files:
    os.rename(f, f"{int(time.time())}_{f}")

# 11. Move files by size (>1MB) to 'large_files' folder
os.makedirs("large_files", exist_ok=True)
for f in os.listdir("."):
    if os.path.isfile(f) and os.path.getsize(f) > 1_000_000:
        shutil.move(f, "large_files/" + f)

# 12. Replace spaces in filenames with underscores
for f in os.listdir("."):
    new_name = f.replace(" ", "_")
    os.rename(f, new_name)

# 13. Create empty log file for each day
today = time.strftime("%Y-%m-%d")
open(f"log_{today}.txt", "w").close()

# 14. Read all files in a folder and merge into one
with open("merged.txt", "w") as outfile:
    for f in txt_files:
        with open(f) as infile:
            outfile.write(infile.read() + "\n")

# 15. Check for duplicate filenames
names = os.listdir(".")
duplicates = [x for x in names if names.count(x) > 1]
print("Duplicates:", duplicates)

# 16. Move files based on extension to separate folders
for f in os.listdir("."):
    if os.path.isfile(f):
        ext = f.split(".")[-1]
        os.makedirs(ext, exist_ok=True)
        shutil.move(f, f"{ext}/{f}")

# 17. Find empty files
empty_files = [f for f in os.listdir(".") if os.path.isfile(f) and os.path.getsize(f) == 0]
print("Empty files:", empty_files)

# 18. Backup folder recursively
shutil.copytree("source_folder", "backup_folder")

# 19. List files with creation date
for f in os.listdir("."):
    ctime = time.ctime(os.path.getctime(f))
    print(f, ctime)

# 20. Delete files older than 7 days
import datetime
now = time.time()
for f in os.listdir("."):
    if os.path.isfile(f) and now - os.path.getctime(f) > 7*24*3600:
        os.remove(f)
----------------------------------------------
# Example 401: Download file from URL
import requests
url = "https://example.com/file.txt"
r = requests.get(url)
with open("file.txt", "wb") as f:
    f.write(r.content)

# Example 402: Fetch JSON from API
response = requests.get("https://api.example.com/data")
data = response.json()
print(data)

# Example 403: Web scraping using BeautifulSoup
from bs4 import BeautifulSoup
html = "<html><body><p>Hello</p></body></html>"
soup = BeautifulSoup(html, "html.parser")
print(soup.p.text)
----------------------------------------------
Submit a form using requests

payload = {"username": "user", "password": "pass"}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)
----------------------------------------------
Run a shell command

import subprocess
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)
print(result.returncode)
print(result.stderr)
----------------------------------------------
Delete a folder

import os
os.rmdir("new_folder")
----------------------------------------------
Read environment variables

import os
print(os.environ.get("PATH"))
----------------------------------------------
List files sorted by size

import os
files = [f for f in os.listdir(".") if os.path.isfile(f)]
files.sort(key=lambda f: os.path.getsize(f))
print(files)
----------------------------------------------
List files sorted by modification date

import os
files = [f for f in os.listdir(".") if os.path.isfile(f)]
files.sort(key=lambda f: os.path.getmtime(f))
print(files)
----------------------------------------------
Copy folder recursively

import shutil
shutil.copytree("source_folder", "destination_folder")
----------------------------------------------
Delete temporary files recursively

import os, shutil
for root, dirs, files in os.walk("."):
    for f in files:
        if f.endswith(".tmp"):
            os.remove(os.path.join(root, f))
----------------------------------------------
import re

# 1. Extract all email addresses from a string
text = "Contact us at info@example.com or support@site.org"
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print(emails)

# 2. Validate a list of phone numbers (simple US format)
phones = ["123-456-7890", "555-999-8888", "1234567"]
valid_phones = [p for p in phones if re.fullmatch(r'\d{3}-\d{3}-\d{4}', p)]
print(valid_phones)

# 3. Find all URLs in a text file
text = "Visit https://example.com and http://site.org"
urls = re.findall(r'https?://[^\s]+', text)
print(urls)

# 4. Replace multiple spaces with a single space
s = "This   is   spaced"
cleaned = re.sub(r'\s+', ' ', s)
print(cleaned)

# 5. Remove all HTML tags from a string
html = "<p>Hello <b>World</b></p>"
text_only = re.sub(r'<.*?>', '', html)
print(text_only)

# 6. Extract hashtags from tweets
tweet = "Loving #Python and #AI"
hashtags = re.findall(r'#\w+', tweet)
print(hashtags)

# 7. Detect valid IP addresses
ips = ["192.168.0.1", "256.0.0.1"]
valid_ips = [ip for ip in ips if re.fullmatch(r'(?:\d{1,3}\.){3}\d{1,3}', ip)]
print(valid_ips)

# 8. Split a text by punctuation marks
text = "Hello, world! How are you?"
words = re.split(r'[,.!?]\s*', text)
print(words)

# 9. Validate date strings (YYYY-MM-DD)
dates = ["2023-03-07", "07-03-2023"]
valid_dates = [d for d in dates if re.fullmatch(r'\d{4}-\d{2}-\d{2}', d)]
print(valid_dates)

# 10. Find all words starting with a capital letter
text = "Hello World from Python"
caps = re.findall(r'\b[A-Z][a-z]*\b', text)
print(caps)

# 11. Extract all numeric values from a string
text = "There are 12 apples and 30 oranges"
nums = re.findall(r'\d+', text)
print(nums)

# 12. Detect repeated words in a text
text = "This is is repeated"
repeats = re.findall(r'\b(\w+)\s+\1\b', text)
print(repeats)

# 13. Replace all digits with #
s = "My phone is 123-456-7890"
masked = re.sub(r'\d', '#', s)
print(masked)

# 14. Extract domain names from URLs
urls = ["https://example.com/path", "http://site.org"]
domains = [re.search(r'https?://([^/]+)', u).group(1) for u in urls]
print(domains)

# 15. Validate hexadecimal color codes
colors = ["#FFF", "#123ABC", "123456"]
valid_colors = [c for c in colors if re.fullmatch(r'#(?:[0-9A-Fa-f]{3}){1,2}', c)]
print(valid_colors)

# 16. Remove all non-alphanumeric characters
s = "Hello, World! 123"
cleaned = re.sub(r'[^A-Za-z0-9 ]+', '', s)
print(cleaned)

# 17. Detect time in HH:MM format
times = ["12:30", "24:60", "09:15"]
valid_times = [t for t in times if re.fullmatch(r'([01]\d|2[0-3]):[0-5]\d', t)]
print(valid_times)

# 18. Extract all mentions (e.g., @username)
tweet = "Hello @user1 and @user2"
mentions = re.findall(r'@\w+', tweet)
print(mentions)

# 19. Find words that end with a specific suffix
text = "I like running, swimming, coding"
suffix_words = re.findall(r'\b\w+ing\b', text)
print(suffix_words)

# 20. Validate US ZIP codes
zips = ["12345", "12345-6789", "ABCDE"]
valid_zips = [z for z in zips if re.fullmatch(r'\d{5}(-\d{4})?', z)]
print(valid_zips)

# 21. Replace dates in text with ISO format
text = "Today is 07/03/2026"
converted = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\2-\1', text)
print(converted)

# 22. Extract prices from receipts
text = "Item A $12.50, Item B $7.99"
prices = re.findall(r'\$\d+\.\d{2}', text)
print(prices)

# 23. Check for valid credit card numbers (simple pattern)
cards = ["1234-5678-9012-3456", "1234 5678 9012 3456"]
valid_cards = [c for c in cards if re.fullmatch(r'(\d{4}[- ]?){3}\d{4}', c)]
print(valid_cards)

# 24. Extract filenames from file paths
paths = ["/home/user/file.txt", "C:\\folder\\data.csv"]
filenames = [re.search(r'[^\\/]+$', p).group(0) for p in paths]
print(filenames)

# 25. Replace multiple newlines with a single newline
text = "Line1\n\n\nLine2"
single_newline = re.sub(r'\n+', '\n', text)
print(single_newline)

# 26. Find all words of a certain length
text = "I love Python programming"
words = re.findall(r'\b\w{6}\b', text)
print(words)

# 27. Extract all JSON-like key-value patterns
text = '{"name": "John", "age": 30}'
kv_pairs = re.findall(r'"(\w+)":\s*"?(.*?)"?[,}]', text)
print(kv_pairs)

# 28. Detect duplicate lines in a text
text = "Hello\nWorld\nHello\nPython"
lines = text.split('\n')
duplicates = set([line for line in lines if lines.count(line) > 1])
print(duplicates)

# 29. Validate strong passwords (min 8 chars, digit, uppercase)
pwds = ["Password1", "weak", "StrongPass2"]
strong = [p for p in pwds if re.fullmatch(r'(?=.*[A-Z])(?=.*\d).{8,}', p)]
print(strong)

# 30. Extract HTML <a> tag href values
html = '<a href="https://example.com">Link</a>'
hrefs = re.findall(r'<a\s+href="([^"]+)"', html)
print(hrefs)

# 31. Find all hexadecimal numbers in a file
text = "Colors: 0xFF, 0x1A3B"
hex_nums = re.findall(r'0x[0-9A-Fa-f]+', text)
print(hex_nums)

# 32. Extract content between brackets [...]
text = "List: [item1, item2, item3]"
content = re.findall(r'\[(.*?)\]', text)
print(content)

# 33. Validate MAC addresses
macs = ["00:1A:2B:3C:4D:5E", "001A2B3C4D5E"]
valid_macs = [m for m in macs if re.fullmatch(r'(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}', m)]
print(valid_macs)

# 34. Split a string at capital letters
s = "CamelCaseWord"
split_words = re.findall(r'[A-Z][a-z]*', s)
print(split_words)

# 35. Convert snake_case to camelCase in a string
s = "this_is_snake_case"
camel = re.sub(r'_(\w)', lambda m: m.group(1).upper(), s)
print(camel)
----------------------------------------------

----------------------------------------------

----------------------------------------------

----------------------------------------------

----------------------------------------------

----------------------------------------------