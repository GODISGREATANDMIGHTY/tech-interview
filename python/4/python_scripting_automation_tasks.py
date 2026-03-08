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

----------------------------------------------

----------------------------------------------

----------------------------------------------

----------------------------------------------

----------------------------------------------

----------------------------------------------