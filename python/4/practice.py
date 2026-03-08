Python Automation & Scripting Examples (1–100)
Category A: Regex & Text Processing (1–25)
import re

# 1. Extract all email addresses from a string
text = "Contact: alice@example.com, bob@test.org"
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print(emails)

# 2. Validate a US phone number (XXX-XXX-XXXX)
phones = ["123-456-7890", "999-999-999"]
valid_phones = [p for p in phones if re.fullmatch(r'\d{3}-\d{3}-\d{4}', p)]
print(valid_phones)

# 3. Find all URLs in a text
text = "Visit https://site.com or http://example.org"
urls = re.findall(r'https?://[^\s]+', text)
print(urls)

# 4. Replace multiple spaces with a single space
s = "This   is   spaced"
s_clean = re.sub(r'\s+', ' ', s)
print(s_clean)

# 5. Remove all HTML tags
html = "<p>Hello <b>World</b></p>"
text_only = re.sub(r'<.*?>', '', html)
print(text_only)

# 6. Extract hashtags from a tweet
tweet = "Loving #Python #Automation"
hashtags = re.findall(r'#\w+', tweet)
print(hashtags)

# 7. Detect valid IP addresses
ips = ["192.168.1.1", "256.0.0.1"]
valid_ips = [ip for ip in ips if re.fullmatch(r'(?:\d{1,3}\.){3}\d{1,3}', ip)]
print(valid_ips)

# 8. Split text by punctuation
text = "Hello, world! How are you?"
words = re.split(r'[,.!?]\s*', text)
print(words)

# 9. Validate date strings YYYY-MM-DD
dates = ["2026-03-07", "07-03-2026"]
valid_dates = [d for d in dates if re.fullmatch(r'\d{4}-\d{2}-\d{2}', d)]
print(valid_dates)

# 10. Find words starting with capital letters
text = "Python is Fun"
caps = re.findall(r'\b[A-Z][a-z]*\b', text)
print(caps)

# 11. Extract numeric values
text = "There are 12 apples and 30 oranges"
numbers = re.findall(r'\d+', text)
print(numbers)

# 12. Detect repeated words
text = "This is is repeated"
repeats = re.findall(r'\b(\w+)\s+\1\b', text)
print(repeats)

# 13. Replace digits with #
s = "My phone: 123-456-7890"
masked = re.sub(r'\d', '#', s)
print(masked)

# 14. Extract domain from URL
urls = ["https://example.com/path", "http://site.org"]
domains = [re.search(r'https?://([^/]+)', u).group(1) for u in urls]
print(domains)

# 15. Validate hexadecimal color codes
colors = ["#FFF", "#123ABC", "123456"]
valid_colors = [c for c in colors if re.fullmatch(r'#(?:[0-9A-Fa-f]{3}){1,2}', c)]
print(valid_colors)

# 16. Remove non-alphanumeric characters
s = "Hello, World! 123"
cleaned = re.sub(r'[^A-Za-z0-9 ]+', '', s)
print(cleaned)

# 17. Detect time HH:MM format
times = ["12:30", "24:60", "09:15"]
valid_times = [t for t in times if re.fullmatch(r'([01]\d|2[0-3]):[0-5]\d', t)]
print(valid_times)

# 18. Extract mentions @username
tweet = "Hello @user1 @user2"
mentions = re.findall(r'@\w+', tweet)
print(mentions)

# 19. Words ending with 'ing'
text = "I like running, swimming, coding"
ing_words = re.findall(r'\b\w+ing\b', text)
print(ing_words)

# 20. Validate US ZIP codes
zips = ["12345", "12345-6789", "ABCDE"]
valid_zips = [z for z in zips if re.fullmatch(r'\d{5}(-\d{4})?', z)]
print(valid_zips)

# 21. Replace dates in text to ISO format
text = "Today: 07/03/2026"
iso_date = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\2-\1', text)
print(iso_date)

# 22. Extract prices
text = "Item A $12.50, Item B $7.99"
prices = re.findall(r'\$\d+\.\d{2}', text)
print(prices)

# 23. Validate credit card numbers
cards = ["1234-5678-9012-3456", "1234 5678 9012 3456"]
valid_cards = [c for c in cards if re.fullmatch(r'(\d{4}[- ]?){3}\d{4}', c)]
print(valid_cards)

# 24. Extract filenames from paths
paths = ["/home/user/file.txt", "C:\\folder\\data.csv"]
files = [re.search(r'[^\\/]+$', p).group(0) for p in paths]
print(files)

# 25. Remove duplicate words in a string
text = "hello hello world world"
unique_words = ' '.join(dict.fromkeys(text.split()))
print(unique_words)




26–50: File Handling & OS Automation
import os
import shutil
from datetime import datetime, timedelta

# 26. Read a file and print lines
with open('example.txt') as f:
    print(f.readlines())

# 27. Count words in a file
with open('example.txt') as f:
    word_count = len(f.read().split())
print(word_count)

# 28. Count characters frequency
from collections import Counter
with open('example.txt') as f:
    counter = Counter(f.read())
print(counter.most_common(5))

# 29. Copy a file
shutil.copyfile('example.txt', 'copy.txt')

# 30. Move a file
shutil.move('copy.txt', 'moved.txt')

# 31. Delete a file
os.remove('moved.txt') if os.path.exists('moved.txt') else None

# 32. Create a directory
os.makedirs('folder/subfolder', exist_ok=True)

# 33. List files in a directory
print(os.listdir('folder'))

# 34. Rename a file
os.rename('example.txt', 'example_renamed.txt')

# 35. Check if file exists
print(os.path.exists('example_renamed.txt'))

# 36. Read all CSV rows as lists
with open('data.csv') as f:
    rows = [line.strip().split(',') for line in f]
print(rows[:3])

# 37. Append text to a file
with open('log.txt', 'a') as f:
    f.write("New log entry\n")

# 38. Read last N lines of a file
with open('log.txt') as f:
    lines = f.readlines()
print(lines[-5:])

# 39. Remove empty lines from a file
with open('log.txt') as f:
    non_empty = [l for l in f if l.strip()]
with open('log_clean.txt', 'w') as f:
    f.writelines(non_empty)

# 40. Merge multiple text files
files = ['a.txt','b.txt']
with open('merged.txt','w') as out:
    for f in files:
        out.write(open(f).read() + '\n')

# 41. Replace all tabs with spaces
with open('tabbed.txt') as f:
    text = f.read()
text = text.replace('\t','    ')
with open('tabbed.txt','w') as f:
    f.write(text)

# 42. Find longest line in a file
with open('example_renamed.txt') as f:
    print(max(f, key=len))

# 43. Backup all files in folder
backup_dir = 'backup'
os.makedirs(backup_dir, exist_ok=True)
for f in os.listdir('folder'):
    shutil.copy(os.path.join('folder', f), backup_dir)

# 44. Delete files older than 7 days
cutoff = datetime.now() - timedelta(days=7)
for f in os.listdir('folder'):
    path = os.path.join('folder', f)
    if os.path.isfile(path) and datetime.fromtimestamp(os.path.getmtime(path)) < cutoff:
        os.remove(path)

# 45. Count total words in folder files
total_words = 0
for f in os.listdir('folder'):
    with open(os.path.join('folder',f)) as file:
        total_words += len(file.read().split())
print(total_words)

# 46. Detect duplicate lines
with open('example_renamed.txt') as f:
    lines = f.read().splitlines()
dupes = set([l for l in lines if lines.count(l)>1])
print(dupes)

# 47. Read JSON file
import json
with open('data.json') as f:
    data = json.load(f)
print(data)

# 48. Write JSON file
with open('output.json','w') as f:
    json.dump({'name':'Alice','age':30}, f, indent=2)

# 49. Replace a word in file
with open('example_renamed.txt') as f:
    text = f.read()
text = text.replace('old','new')
with open('example_renamed.txt','w') as f:
    f.write(text)

# 50. Move all .txt files to subfolder
os.makedirs('txt_files', exist_ok=True)
for f in os.listdir('folder'):
    if f.endswith('.txt'):
        shutil.move(os.path.join('folder',f), 'txt_files')




51–75: Data Parsing & Transformation
import csv
import json
from collections import defaultdict

# 51. Parse CSV without csv module
with open('data.csv') as f:
    data = [line.strip().split(',') for line in f]
print(data[:3])

# 52. Extract specific column from CSV
with open('data.csv') as f:
    column = [line.strip().split(',')[1] for line in f]
print(column[:5])

# 53. Convert CSV to JSON
with open('data.csv') as f:
    rows = [line.strip().split(',') for line in f]
keys = rows[0]
json_data = [dict(zip(keys,row)) for row in rows[1:]]
print(json_data[:2])

# 54. Flatten nested dict
nested = {'a':{'b':{'c':1}}}
flat = {}
def flatten(d, prefix=''):
    for k,v in d.items():
        if isinstance(v, dict):
            flatten(v, prefix+k+'.')
        else:
            flat[prefix+k]=v
flatten(nested)
print(flat)

# 55. Parse JSON string
s = '{"user":{"name":"Alice","age":30}}'
data = json.loads(s)
print(data['user']['name'])

# 56. Convert dict to CSV
data = [{'name':'Alice','age':30},{'name':'Bob','age':25}]
with open('out.csv','w') as f:
    f.write(','.join(data[0].keys())+'\n')
    for d in data:
        f.write(','.join(str(v) for v in d.values())+'\n')

# 57. Read TSV file
with open('data.tsv') as f:
    tsv_data = [line.strip().split('\t') for line in f]
print(tsv_data[:3])

# 58. Extract key-value pairs from text
text = "name:Alice\nage:30"
kv = dict([line.split(':') for line in text.splitlines()])
print(kv)

# 59. Parse dates from text
from datetime import datetime
dates = ["07-03-2026","2026/03/07"]
parsed = [datetime.strptime(d,"%d-%m-%Y") if '-' in d else datetime.strptime(d,"%Y/%m/%d") for d in dates]
print(parsed)

# 60. Count frequency of words in text
from collections import Counter
text = "Python Python scripting automation"
freq = Counter(text.split())
print(freq)

# 61. Extract all numbers from text
text = "I have 12 apples and 30 oranges"
numbers = [int(n) for n in text.split() if n.isdigit()]
print(numbers)

# 62. Replace multiple spaces with single
s = "Python    scripting  automation"
s_clean = ' '.join(s.split())
print(s_clean)

# 63. Detect duplicate keys in list of dicts
data = [{'name':'Alice'},{'name':'Bob'},{'name':'Alice'}]
seen = set()
duplicates = [d for d in data if d['name'] in seen or seen.add(d['name'])]
print(duplicates)

# 64. Convert list of dicts to dict by key
data = [{'id':1,'name':'A'},{'id':2,'name':'B'}]
by_id = {d['id']:d['name'] for d in data}
print(by_id)

# 65. Extract substrings between brackets
text = "This is [sample] text"
import re
matches = re.findall(r'\[(.*?)\]', text)
print(matches)

# 66. Extract numeric values with regex
text = "Price: $123.45, Tax: $6.78"
nums = re.findall(r'\d+\.\d+', text)
print(nums)

# 67. Split string by comma or semicolon
s = "apple,banana;orange"
parts = re.split(r'[;,]', s)
print(parts)

# 68. Convert snake_case to camelCase
s = "my_variable_name"
camel = ''.join([s.split('_')[0]] + [x.capitalize() for x in s.split('_')[1:]])
print(camel)

# 69. Validate MAC address
macs = ["00:1A:2B:3C:4D:5E","00-1A-2B-3C-4D-5E"]
valid = [m for m in macs if re.fullmatch(r'([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}',m)]
print(valid)

# 70. Parse configuration file
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
print(config['DEFAULT'])

# 71. Extract JSON keys recursively
nested_json = {'a':{'b':{'c':1}}}
keys=[]
def get_keys(d):
    for k,v in d.items():
        keys.append(k)
        if isinstance(v,dict):
            get_keys(v)
get_keys(nested_json)
print(keys)

# 72. Remove lines containing a word
lines = ["keep this","delete this"]
cleaned = [l for l in lines if 'delete' not in l]
print(cleaned)

# 73. Merge multiple dicts
d1 = {'a':1}
d2 = {'b':2}
merged = {**d1,**d2}
print(merged)

# 74. Convert list of tuples to dict
tuples = [('a',1),('b',2)]
d = dict(tuples)
print(d)

# 75. Count unique elements in list
lst = [1,2,2,3,1,4]
unique_count = len(set(lst))
print(unique_count)




76–100: CLI & System Automation
import os
import subprocess
import sys
from datetime import datetime

# 76. Execute shell command
subprocess.run(['echo','Hello World'])

# 77. Get current working directory
print(os.getcwd())

# 78. List all files with .txt extension
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print(txt_files)

# 79. Check OS platform
print(sys.platform)

# 80. Get environment variables
print(os.environ.get('PATH'))

# 81. Create timestamped log file
log_name = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
with open(log_name,'w') as f:
    f.write("Log started\n")

# 82. Schedule a script (simulate with sleep)
import time
print("Waiting 2 seconds...")
time.sleep(2)
print("Done")

# 83. Count files in a directory
file_count = len([f for f in os.listdir('.') if os.path.isfile(f)])
print(file_count)

# 84. Recursively list files
for root, dirs, files in os.walk('.'):
    print(root, files[:3])

# 85. Delete empty directories
for root, dirs, files in os.walk('.'):
    for d in dirs:
        path = os.path.join(root,d)
        if not os.listdir(path):
            os.rmdir(path)

# 86. Read command-line arguments
print(sys.argv)

# 87. Redirect output to a file
with open('out.txt','w') as f:
    print("Hello File", file=f)

# 88. Get file size
print(os.path.getsize('example.txt'))

# 89. Check if path is file or folder
path = 'example.txt'
print(os.path.isfile(path), os.path.isdir(path))

# 90. List only directories
dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
print(dirs)

# 91. Copy entire folder
shutil.copytree('folder','folder_backup',dirs_exist_ok=True)

# 92. Remove folder recursively
shutil.rmtree('folder_backup',ignore_errors=True)

# 93. Get file modification time
mtime = datetime.fromtimestamp(os.path.getmtime('example.txt'))
print(mtime)

# 94. Change file permissions
os.chmod('example.txt', 0o644)

# 95. Create multiple folders in loop
for i in range(3):
    os.makedirs(f"dir_{i}",exist_ok=True)

# 96. Move file with rename
shutil.move('example.txt','dir_0/example.txt')

# 97. Get system arguments count
print(len(sys.argv))

# 98. Exit program with status
# sys.exit(0)  # commented to allow rest to run

# 99. Print Python version
print(sys.version)

# 100. Measure script execution time
start=time.time()
sum(range(10000))
print("Execution time:",time.time()-start)




101–140: Web Scraping & HTML Parsing (Standard Library Only)
import urllib.request
from html.parser import HTMLParser

# 101. Fetch webpage
url = "http://example.com"
with urllib.request.urlopen(url) as response:
    html = response.read().decode()
print(html[:100])

# 102. Simple HTML parser to extract titles
class TitleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.title = ''
    def handle_starttag(self, tag, attrs):
        if tag=='title': self.in_title=True
    def handle_endtag(self, tag):
        if tag=='title': self.in_title=False
    def handle_data(self, data):
        if self.in_title: self.title+=data
parser=TitleParser()
parser.feed(html)
print(parser.title)

# 103. Extract all links
class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
    def handle_starttag(self, tag, attrs):
        if tag=='a':
            href=[v for k,v in attrs if k=='href']
            if href: self.links.append(href[0])
link_parser=LinkParser()
link_parser.feed(html)
print(link_parser.links[:5])

# 104. Extract all images
class ImgParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images=[]
    def handle_starttag(self, tag, attrs):
        if tag=='img':
            src=[v for k,v in attrs if k=='src']
            if src: self.images.append(src[0])
img_parser=ImgParser()
img_parser.feed(html)
print(img_parser.images[:5])

# 105. Extract paragraphs
class PParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text=[]
        self.in_p=False
    def handle_starttag(self, tag, attrs):
        if tag=='p': self.in_p=True
    def handle_endtag(self, tag):
        if tag=='p': self.in_p=False
    def handle_data(self, data):
        if self.in_p: self.text.append(data.strip())
p_parser=PParser()
p_parser.feed(html)
print(p_parser.text[:5])

# 106. Extract headings
class HParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.headings=[]
        self.in_h=False
    def handle_starttag(self, tag, attrs):
        if tag in ['h1','h2','h3','h4','h5','h6']: self.in_h=tag
    def handle_endtag(self, tag):
        if tag==self.in_h: self.in_h=False
    def handle_data(self, data):
        if self.in_h: self.headings.append(data.strip())
h_parser=HParser()
h_parser.feed(html)
print(h_parser.headings)

# 107. Extract forms and inputs
class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inputs=[]
    def handle_starttag(self, tag, attrs):
        if tag=='input':
            name=[v for k,v in attrs if k=='name']
            if name: self.inputs.append(name[0])
form_parser=FormParser()
form_parser.feed(html)
print(form_parser.inputs[:5])

# 108. Extract meta tags
class MetaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.metas=[]
    def handle_starttag(self, tag, attrs):
        if tag=='meta':
            self.metas.append(dict(attrs))
meta_parser=MetaParser()
meta_parser.feed(html)
print(meta_parser.metas[:5])

# 109. Extract text from HTML ignoring tags
class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text=[]
    def handle_data(self, data):
        self.text.append(data.strip())
text_parser=TextParser()
text_parser.feed(html)
print(' '.join([t for t in text_parser.text if t]))

# 110. Extract links containing keyword
keyword_links=[link for link in link_parser.links if 'blog' in link]
print(keyword_links[:5])

# 111. Extract images with .png extension
png_images=[img for img in img_parser.images if img.endswith('.png')]
print(png_images[:5])

# 112. Extract links with regex
import re
links_regex=re.findall(r'href="([^"]+)"', html)
print(links_regex[:5])

# 113. Extract all scripts
scripts=re.findall(r'<script.*?src="(.*?)".*?>', html)
print(scripts)

# 114. Extract stylesheets
stylesheets=re.findall(r'<link.*?href="(.*?)".*?>', html)
print(stylesheets)

# 115. Extract tables (simplified)
tables=re.findall(r'<table.*?>(.*?)</table>', html, re.DOTALL)
print(tables[:1])

# 116. Extract rows and columns from table
if tables:
    rows=re.findall(r'<tr.*?>(.*?)</tr>', tables[0], re.DOTALL)
    table_data=[[td.strip() for td in re.findall(r'<t[dh].*?>(.*?)</t[dh]>', r, re.DOTALL)] for r in rows]
    print(table_data[:3])

# 117. Extract links from tables
if tables:
    links_in_table=[re.findall(r'href="(.*?)"', r) for r in rows]
    print(links_in_table[:2])

# 118. Extract list items
lis=re.findall(r'<li.*?>(.*?)</li>', html, re.DOTALL)
print(lis[:5])

# 119. Extract bold texts
bolds=re.findall(r'<b.*?>(.*?)</b>', html)
print(bolds[:5])

# 120. Extract italic texts
italics=re.findall(r'<i.*?>(.*?)</i>', html)
print(italics[:5])

# 121. Extract divs with specific class
divs=re.findall(r'<div class="content".*?>(.*?)</div>', html, re.DOTALL)
print(divs[:3])

# 122. Extract span with specific class
spans=re.findall(r'<span class="author".*?>(.*?)</span>', html)
print(spans[:5])

# 123. Extract links from nested divs
nested_links=re.findall(r'<div.*?>(<a.*?>.*?</a>)</div>', html, re.DOTALL)
print(nested_links[:3])

# 124. Extract comments
comments=re.findall(r'<!--(.*?)-->', html, re.DOTALL)
print(comments[:2])

# 125. Extract DOCTYPE
doctype=re.findall(r'<!DOCTYPE (.*?)>', html)
print(doctype)

# 126. Extract all h1 text
h1_text=re.findall(r'<h1.*?>(.*?)</h1>', html)
print(h1_text)

# 127. Extract all h2 text
h2_text=re.findall(r'<h2.*?>(.*?)</h2>', html)
print(h2_text)

# 128. Extract alt attributes of images
alts=re.findall(r'<img.*?alt="(.*?)".*?>', html)
print(alts[:5])

# 129. Extract links without http
local_links=[l for l in link_parser.links if not l.startswith('http')]
print(local_links[:5])

# 130. Count number of links
print(len(link_parser.links))

# 131. Count number of images
print(len(img_parser.images))

# 132. Extract first table
first_table=tables[0] if tables else ''
print(first_table[:100])

# 133. Extract first paragraph
first_paragraph=lis[0] if lis else ''
print(first_paragraph)

# 134. Extract first heading
first_heading=h1_text[0] if h1_text else ''
print(first_heading)

# 135. Extract scripts without src
inline_scripts=re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
print(inline_scripts[:2])

# 136. Extract links inside a specific div class
div_content=re.findall(r'<div class="sidebar">(.*?)</div>', html, re.DOTALL)
div_links=[re.findall(r'href="(.*?)"', d) for d in div_content]
print(div_links[:2])

# 137. Extract all attributes of img tags
all_img_attrs=re.findall(r'<img(.*?)>', html)
print(all_img_attrs[:3])

# 138. Extract all form actions
forms=re.findall(r'<form.*?action="(.*?)".*?>', html)
print(forms[:2])

# 139. Extract script type attributes
script_types=re.findall(r'<script.*?type="(.*?)".*?>', html)
print(script_types[:3])

# 140. Extract first 100 chars of visible text
visible_text=' '.join([t for t in text_parser.text if t]).strip()
print(visible_text[:100])




141–220: Advanced File / OS Automation (80 examples)
import os
import shutil
from datetime import datetime, timedelta

# 141. Recursively find all .txt files
txt_files = [os.path.join(root, f) for root, _, files in os.walk('.') for f in files if f.endswith('.txt')]
print(txt_files[:5])

# 142. Rename all .txt files to .bak
for f in txt_files:
    os.rename(f, f.replace('.txt','.bak'))

# 143. Move all .bak files to backup folder
os.makedirs('backup', exist_ok=True)
for f in txt_files:
    shutil.move(f.replace('.txt','.bak'), 'backup/')

# 144. Delete files older than 30 days
cutoff = datetime.now() - timedelta(days=30)
for root, _, files in os.walk('backup'):
    for f in files:
        path = os.path.join(root,f)
        if datetime.fromtimestamp(os.path.getmtime(path)) < cutoff:
            os.remove(path)

# 145. Create folder hierarchy dynamically
folders = ['data','logs','reports']
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# 146. Copy only .csv files to folder
for root, _, files in os.walk('.'):
    for f in files:
        if f.endswith('.csv'):
            shutil.copy(os.path.join(root,f), 'data/')

# 147. Merge multiple text files into one
with open('merged.txt','w') as out:
    for root, _, files in os.walk('data'):
        for f in files:
            if f.endswith('.txt'):
                with open(os.path.join(root,f)) as infile:
                    out.write(infile.read() + '\n')

# 148. Count total number of files in a directory recursively
total_files = sum([len(files) for _,_,files in os.walk('.')])
print(total_files)

# 149. Delete empty folders
for root, dirs, _ in os.walk('.'):
    for d in dirs:
        path = os.path.join(root,d)
        if not os.listdir(path):
            os.rmdir(path)

# 150. List directories sorted by name
dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
dirs.sort()
print(dirs)

# 151. Move files based on prefix
for f in os.listdir('data'):
    if f.startswith('log'):
        shutil.move(os.path.join('data',f),'logs/')

# 152. Backup files with timestamp
for f in os.listdir('data'):
    shutil.copy(os.path.join('data',f), f"backup/{f}_{datetime.now().strftime('%Y%m%d_%H%M%S')}")

# 153. Replace spaces in filenames with underscore
for f in os.listdir('data'):
    new_name = f.replace(' ','_')
    os.rename(os.path.join('data',f), os.path.join('data',new_name))

# 154. Count files by extension
ext_count = {}
for root, _, files in os.walk('.'):
    for f in files:
        ext = f.split('.')[-1]
        ext_count[ext] = ext_count.get(ext,0)+1
print(ext_count)

# 155. Create empty files
for i in range(5):
    open(f'empty_{i}.txt','w').close()

# 156. Move files to subfolders by extension
for f in os.listdir('data'):
    ext = f.split('.')[-1]
    os.makedirs(f'data/{ext}', exist_ok=True)
    shutil.move(os.path.join('data',f), f'data/{ext}/{f}')

# 157. Count lines in all files
total_lines = 0
for root, _, files in os.walk('data'):
    for f in files:
        with open(os.path.join(root,f)) as file:
            total_lines += sum(1 for _ in file)
print(total_lines)

# 158. List largest 5 files
file_sizes = [(f,os.path.getsize(f)) for f in os.listdir('.') if os.path.isfile(f)]
file_sizes.sort(key=lambda x:x[1], reverse=True)
print(file_sizes[:5])

# 159. Find recently modified files (last 24h)
recent_files = [f for f in os.listdir('.') if os.path.isfile(f) and (datetime.now()-datetime.fromtimestamp(os.path.getmtime(f))).days<1]
print(recent_files)

# 160. Archive files older than 7 days
archive_folder = 'archive'
os.makedirs(archive_folder, exist_ok=True)
for f in os.listdir('.'):
    if os.path.isfile(f) and (datetime.now()-datetime.fromtimestamp(os.path.getmtime(f))).days>7:
        shutil.move(f, archive_folder)

# 161. Copy folder structure without files
def copy_structure(src,dest):
    for root, dirs, _ in os.walk(src):
        for d in dirs:
            os.makedirs(os.path.join(dest,os.path.relpath(os.path.join(root,d),src)), exist_ok=True)
copy_structure('data','data_structure_copy')

# 162. Replace file extension recursively
for root, _, files in os.walk('data'):
    for f in files:
        old = os.path.join(root,f)
        new = os.path.join(root,f.rsplit('.',1)[0]+'.bak')
        os.rename(old,new)

# 163. Delete temporary files (.tmp)
for root, _, files in os.walk('.'):
    for f in files:
        if f.endswith('.tmp'): os.remove(os.path.join(root,f))

# 164. List hidden files
hidden_files = [f for f in os.listdir('.') if f.startswith('.')]
print(hidden_files)

# 165. Generate file report (name, size, modified)
report = [(f,os.path.getsize(f),datetime.fromtimestamp(os.path.getmtime(f))) for f in os.listdir('.') if os.path.isfile(f)]
print(report[:5])

# 166. Merge files with header skipping first line
with open('combined.txt','w') as out:
    for f in os.listdir('data'):
        if f.endswith('.txt'):
            with open(os.path.join('data',f)) as infile:
                next(infile)
                out.write(infile.read())

# 167. Read last N bytes of file
with open('combined.txt','rb') as f:
    f.seek(-50,2)
    print(f.read())

# 168. Count word occurrences in all files
word_count = {}
for f in os.listdir('data'):
    if f.endswith('.txt'):
        with open(os.path.join('data',f)) as file:
            for w in file.read().split():
                word_count[w] = word_count.get(w,0)+1
print(sorted(word_count.items(),key=lambda x:x[1],reverse=True)[:5])

# 169. Detect duplicate filenames
names = [f for f in os.listdir('data') if os.path.isfile(os.path.join('data',f))]
duplicates = set([f for f in names if names.count(f)>1])
print(duplicates)

# 170. List files with specific pattern
pattern_files = [f for f in os.listdir('data') if f.startswith('log_')]
print(pattern_files)

# 171. Count subfolders recursively
subfolder_count = sum([len(dirs) for _, dirs, _ in os.walk('.')])
print(subfolder_count)

# 172. Flatten folder to single folder
for root, _, files in os.walk('data'):
    for f in files:
        shutil.move(os.path.join(root,f),'data_flat/'+f)

# 173. Read first line of all files
for f in os.listdir('data'):
    with open(os.path.join('data',f)) as file:
        print(file.readline().strip())

# 174. Get file creation time
for f in os.listdir('data'):
    print(f,datetime.fromtimestamp(os.path.getctime(os.path.join('data',f))))

# 175. Backup files using timestamp
for f in os.listdir('data'):
    shutil.copy(os.path.join('data',f), f"backup/{f}_{datetime.now().strftime('%Y%m%d')}")

# 176. Move files by date modified
for f in os.listdir('data'):
    mod_time = datetime.fromtimestamp(os.path.getmtime(os.path.join('data',f))).strftime('%Y-%m-%d')
    os.makedirs(f"data_by_date/{mod_time}",exist_ok=True)
    shutil.move(os.path.join('data',f), f"data_by_date/{mod_time}/{f}")

# 177. Remove files with certain size
for f in os.listdir('data'):
    if os.path.getsize(os.path.join('data',f))==0:
        os.remove(os.path.join('data',f))

# 178. List all symlinks
symlinks = [f for f in os.listdir('.') if os.path.islink(f)]
print(symlinks)

# 179. Copy files preserving structure
for root, _, files in os.walk('data'):
    for f in files:
        dest = os.path.join('copy_data',os.path.relpath(root,'data'))
        os.makedirs(dest, exist_ok=True)
        shutil.copy(os.path.join(root,f),dest)

# 180. Find largest file in directory
largest_file = max([f for f in os.listdir('data') if os.path.isfile(os.path.join('data',f))], key=lambda x:os.path.getsize(os.path.join('data',x)))
print(largest_file)

# 181–220 would continue similarly with more advanced OS/file tasks:
# e.g., directory syncing, temp file cleanup, file permission changes, recursive backups, automated renaming rules, multi-folder merging, automated logging for file operations, etc.




221–300: Data Parsing & Logs (80 examples)
import csv
import json
import re
from datetime import datetime
from collections import Counter, defaultdict

# 221. Parse CSV and extract a column
with open('data.csv') as f:
    reader = csv.reader(f)
    column = [row[1] for row in reader]
print(column[:5])

# 222. Convert CSV to JSON
with open('data.csv') as f:
    reader = csv.DictReader(f)
    data = list(reader)
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

# 223. Read JSON file and print keys
with open('data.json') as f:
    js = json.load(f)
print(list(js[0].keys()))

# 224. Parse log file and extract errors
errors = []
with open('app.log') as f:
    for line in f:
        if 'ERROR' in line:
            errors.append(line.strip())
print(errors[:5])

# 225. Count occurrences of words in log
word_count = Counter()
with open('app.log') as f:
    for line in f:
        word_count.update(line.strip().split())
print(word_count.most_common(5))

# 226. Extract dates from log lines (YYYY-MM-DD)
dates = []
with open('app.log') as f:
    for line in f:
        match = re.search(r'\d{4}-\d{2}-\d{2}', line)
        if match:
            dates.append(match.group())
print(dates[:5])

# 227. Group log lines by level
logs = defaultdict(list)
with open('app.log') as f:
    for line in f:
        if 'INFO' in line:
            logs['INFO'].append(line.strip())
        elif 'ERROR' in line:
            logs['ERROR'].append(line.strip())
print({k: len(v) for k,v in logs.items()})

# 228. Parse key-value pairs in log
kv_lines = []
with open('app.log') as f:
    for line in f:
        match = re.findall(r'(\w+)=(\w+)', line)
        if match:
            kv_lines.append(dict(match))
print(kv_lines[:3])

# 229. Count unique IPs in log
ips = set()
with open('access.log') as f:
    for line in f:
        match = re.search(r'\b\d+\.\d+\.\d+\.\d+\b', line)
        if match:
            ips.add(match.group())
print(len(ips))

# 230. Extract response codes from server logs
codes = []
with open('access.log') as f:
    for line in f:
        match = re.search(r'"\s(\d{3})\s', line)
        if match:
            codes.append(match.group())
print(codes[:10])

# 231. Summarize log by day
by_day = defaultdict(int)
with open('app.log') as f:
    for line in f:
        match = re.search(r'\d{4}-\d{2}-\d{2}', line)
        if match:
            by_day[match.group()] += 1
print(dict(list(by_day.items())[:5]))

# 232. Parse JSON string from log
line = '{"user":"Alice","action":"login"}'
js = json.loads(line)
print(js['user'])

# 233. Extract numeric values from log
numbers = []
with open('app.log') as f:
    for line in f:
        numbers.extend(re.findall(r'\d+', line))
print(numbers[:5])

# 234. Replace dates in text with ISO format
text = "03/07/2026"
new_text = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\2-\1', text)
print(new_text)

# 235. Detect repeated words in log
with open('app.log') as f:
    for line in f:
        match = re.findall(r'\b(\w+)\s+\1\b', line)
        if match:
            print(match)

# 236. Extract all email addresses from logs
emails = []
with open('app.log') as f:
    for line in f:
        emails.extend(re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', line))
print(emails[:5])

# 237. Parse TSV file
with open('data.tsv') as f:
    tsv_data = [line.strip().split('\t') for line in f]
print(tsv_data[:3])

# 238. Count log lines per level
levels = Counter()
with open('app.log') as f:
    for line in f:
        if 'INFO' in line: levels['INFO'] += 1
        if 'ERROR' in line: levels['ERROR'] += 1
print(levels)

# 239. Extract URL requests from server log
urls = []
with open('access.log') as f:
    for line in f:
        match = re.search(r'GET\s(.*?)\sHTTP', line)
        if match:
            urls.append(match.group(1))
print(urls[:5])

# 240. Summarize most requested URLs
url_count = Counter(urls)
print(url_count.most_common(5))

# 241. Extract JSON key-values recursively
def extract_keys(d, keys=set()):
    for k, v in d.items():
        keys.add(k)
        if isinstance(v, dict):
            extract_keys(v, keys)
    return keys
nested = {"a":{"b":{"c":1}}}
print(extract_keys(nested))

# 242. Parse CSV with inconsistent delimiters
with open('data_inconsistent.csv') as f:
    data = [re.split(r'[,\t;]', line.strip()) for line in f]
print(data[:3])

# 243. Extract first column from CSV
with open('data.csv') as f:
    col1 = [line.strip().split(',')[0] for line in f]
print(col1[:5])

# 244. Merge CSV files into one
import glob
all_rows = []
for filename in glob.glob('*.csv'):
    with open(filename) as f:
        all_rows.extend(f.read().splitlines())
with open('merged.csv','w') as f:
    f.write('\n'.join(all_rows))

# 245. Count JSON objects in file
with open('data.json') as f:
    data = json.load(f)
print(len(data))

# 246. Extract numeric ranges from logs
ranges = []
with open('app.log') as f:
    for line in f:
        match = re.findall(r'\d+-\d+', line)
        if match:
            ranges.extend(match)
print(ranges[:5])

# 247. Detect invalid JSON lines
with open('mixed.jsonl') as f:
    for line in f:
        try:
            json.loads(line)
        except:
            print('Invalid:', line.strip())

# 248. Parse system stats log and average CPU usage
cpu_values = []
with open('system.log') as f:
    for line in f:
        match = re.search(r'CPU:\s(\d+)%', line)
        if match:
            cpu_values.append(int(match.group(1)))
avg_cpu = sum(cpu_values)/len(cpu_values) if cpu_values else 0
print(avg_cpu)

# 249. Extract all IP addresses from logs
ips = set()
with open('access.log') as f:
    for line in f:
        ips.update(re.findall(r'\b\d+\.\d+\.\d+\.\d+\b', line))
print(list(ips)[:5])

# 250. Parse Apache log for status codes
status_count = Counter()
with open('access.log') as f:
    for line in f:
        match = re.search(r'"\s(\d{3})\s', line)
        if match:
            status_count[match.group()] += 1
print(status_count.most_common(5))

# 251–300 would continue similarly:  
# - Parse logs to summarize errors per day  
# - Count occurrences of specific keywords or IP addresses  
# - Extract user agents  
# - Convert logs to CSV/JSON  
# - Filter logs by date ranges  
# - Detect anomalies like repeated failures, spikes, or missing fields  
# - Handle large files efficiently with streaming line processing  
# - Summarize multiple log files into aggregated reports




301–380: Scheduling, Notifications, Emails, Subprocess Automation (80 examples)
import time
import subprocess
import smtplib
from email.message import EmailMessage
from datetime import datetime, timedelta
import os

# 301. Simple delay using time.sleep
print("Start")
time.sleep(2)
print("End after 2 seconds")

# 302. Run a system command
subprocess.run(['echo','Hello from subprocess'])

# 303. Capture output from command
result = subprocess.run(['echo','Capture this'], capture_output=True, text=True)
print(result.stdout.strip())

# 304. Check disk usage
subprocess.run(['df','-h'])

# 305. List directory contents using subprocess
out = subprocess.run(['ls','-l'], capture_output=True, text=True)
print(out.stdout[:100])

# 306. Get current Python version
subprocess.run(['python','--version'])

# 307. Schedule a task after delay
print("Task will run after 3 seconds...")
time.sleep(3)
print("Task executed!")

# 308. Run multiple commands sequentially
commands = [['echo','First'], ['echo','Second']]
for cmd in commands:
    subprocess.run(cmd)

# 309. Run command and check return code
res = subprocess.run(['ls','nonexistentfile'])
print(res.returncode)

# 310. Send email via SMTP (plain example)
msg = EmailMessage()
msg.set_content("This is a test email from Python automation.")
msg['Subject'] = 'Test Email'
msg['From'] = 'sender@example.com'
msg['To'] = 'receiver@example.com'
# Uncomment and configure SMTP to actually send
# with smtplib.SMTP('localhost') as s:
#     s.send_message(msg)

# 311. Retry a command with delay
for i in range(3):
    res = subprocess.run(['ls','nonexistentfile'])
    if res.returncode==0: break
    time.sleep(1)

# 312. Log task execution time
start=time.time()
sum(range(10000))
end=time.time()
print("Execution time:", end-start)

# 313. Send daily report email (skeleton)
def send_report():
    msg = EmailMessage()
    msg.set_content("Daily report.")
    msg['Subject'] = 'Daily Report'
    msg['From'] = 'me@example.com'
    msg['To'] = 'you@example.com'
    # smtp = smtplib.SMTP('localhost')
    # smtp.send_message(msg)
    # smtp.quit()
print("Report sent (simulated)")

# 314. Execute command and capture stderr
res = subprocess.run(['ls','nonexistent'], capture_output=True, text=True)
print("Error:", res.stderr.strip())

# 315. Run a command in background (non-blocking)
subprocess.Popen(['sleep','5'])

# 316. Monitor a file for changes
filename = 'app.log'
last_size = os.path.getsize(filename)
time.sleep(2)
new_size = os.path.getsize(filename)
print("Changed:", new_size != last_size)

# 317. Schedule function at interval
def task():
    print("Task executed at", datetime.now())
for _ in range(3):
    task()
    time.sleep(2)

# 318. Send email with attachment (skeleton)
msg = EmailMessage()
msg['Subject']='Attachment Example'
msg['From']='me@example.com'
msg['To']='you@example.com'
msg.set_content("See attached file.")
# with open('file.txt','rb') as f:
#     msg.add_attachment(f.read(), maintype='text', subtype='plain', filename='file.txt')

# 319. Execute shell command string
subprocess.run("echo Shell String", shell=True)

# 320. Run Python script from another Python script
subprocess.run(['python','script.py'])

# 321. Schedule multiple tasks with different intervals
tasks = [(lambda: print("Task1"),1),(lambda: print("Task2"),2)]
for func,delay in tasks:
    func()
    time.sleep(delay)

# 322. Capture both stdout and stderr
res = subprocess.run(['ls','nonexistent'], capture_output=True, text=True)
print("STDOUT:", res.stdout.strip(), "STDERR:", res.stderr.strip())

# 323. Restart a task if it fails
def run_task():
    res = subprocess.run(['ls','nonexistent'])
    return res.returncode
if run_task()!=0:
    print("Retrying task...")
    time.sleep(1)
    run_task()

# 324. Record execution timestamp to log
with open('execution.log','a') as f:
    f.write(f'Task executed at {datetime.now()}\n')

# 325. Limit task runtime (timeout)
try:
    subprocess.run(['sleep','5'], timeout=2)
except subprocess.TimeoutExpired:
    print("Task timed out")

# 326. Send email with multiple recipients (skeleton)
msg = EmailMessage()
msg['To'] = ','.join(['user1@example.com','user2@example.com'])
msg.set_content("Multi-recipient email")

# 327. Check if service is running via system command
res = subprocess.run(['ps','-ef'], capture_output=True, text=True)
if 'python' in res.stdout: print("Python process running")

# 328. Schedule task based on time of day
if datetime.now().hour==14:
    print("Run afternoon task")

# 329. Log command output to file
with open('cmd_output.log','w') as f:
    subprocess.run(['ls','-l'], stdout=f)

# 330. Send email with CC and BCC (skeleton)
msg = EmailMessage()
msg['Cc'] = 'cc@example.com'
msg['Bcc'] = 'bcc@example.com'
msg.set_content("CC/BCC example")

# 331. Execute multiple shell commands in one string
subprocess.run("echo First && echo Second", shell=True)

# 332. Run long-running task asynchronously
p = subprocess.Popen(['sleep','5'])
print("Task running in background, PID:", p.pid)

# 333. Log errors to separate file
with open('error.log','w') as f:
    subprocess.run(['ls','nonexistent'], stderr=f)

# 334. Monitor log file for ERROR lines
with open('app.log') as f:
    for line in f:
        if 'ERROR' in line:
            print("Error found:", line.strip())

# 335. Schedule weekly task (check weekday)
if datetime.now().weekday()==0:
    print("Monday task executed")

# 336. Automate backup of folder (timestamped)
shutil.make_archive(f"backup_{datetime.now().strftime('%Y%m%d')}", 'zip', 'data')

# 337. Run Python code dynamically
code = "print('Dynamic code executed')"
exec(code)

# 338. Limit subprocess memory usage (Linux example, pseudo)
# subprocess.run(['ulimit','-v','1000000','&&','python','script.py'], shell=True)

# 339. Retry email sending on failure (skeleton)
for _ in range(3):
    try:
        print("Sending email...")
        # send_mail()
        break
    except Exception:
        time.sleep(1)

# 340. Send scheduled notification (simulated)
print(f"Notification: Task completed at {datetime.now()}")

# 341–380 would continue with variations:
# - monitor folder changes
# - periodic report generation
# - send CSV logs via email
# - automated system maintenance scripts
# - subprocess pipelines
# - handle exceptions in automation tasks
# - summarize task results into log files
# - simulate cron jobs using loops and sleep




381–400: Combined Mini Automation Scripts (20 examples)
import os
import re
import csv
import json
import shutil
import subprocess
from datetime import datetime
from email.message import EmailMessage

# 381. Fetch log files, extract ERROR lines, save to CSV
error_rows = []
for f in os.listdir('logs'):
    if f.endswith('.log'):
        with open(os.path.join('logs',f)) as file:
            for line in file:
                if 'ERROR' in line:
                    error_rows.append([f, line.strip()])
with open('errors.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['filename','error'])
    writer.writerows(error_rows)

# 382. Backup CSVs to timestamped folder
os.makedirs('backup_csv',exist_ok=True)
for f in os.listdir('data'):
    if f.endswith('.csv'):
        shutil.copy(os.path.join('data',f), f"backup_csv/{f}_{datetime.now().strftime('%Y%m%d')}")

# 383. Parse multiple JSON files and merge into one
all_data = []
for f in os.listdir('jsons'):
    if f.endswith('.json'):
        with open(os.path.join('jsons',f)) as file:
            all_data.extend(json.load(file))
with open('merged.json','w') as out:
    json.dump(all_data,out,indent=2)

# 384. Read CSV, filter rows, save new CSV
with open('data.csv') as f:
    reader = csv.DictReader(f)
    filtered = [r for r in reader if int(r['age'])>30]
with open('filtered.csv','w',newline='') as f:
    writer = csv.DictWriter(f,fieldnames=filtered[0].keys())
    writer.writeheader()
    writer.writerows(filtered)

# 385. Extract all emails from text files and send summary email (skeleton)
emails = set()
for f in os.listdir('texts'):
    with open(os.path.join('texts',f)) as file:
        emails.update(re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', file.read()))
print("Emails found:", emails)
# msg = EmailMessage()  # configure SMTP and send summary

# 386. Rename files by adding timestamp
for f in os.listdir('data'):
    os.rename(os.path.join('data',f), os.path.join('data', f"{datetime.now().strftime('%Y%m%d')}_{f}"))

# 387. Merge logs, sort by date, save summary
log_lines = []
for f in os.listdir('logs'):
    if f.endswith('.log'):
        with open(os.path.join('logs',f)) as file:
            log_lines.extend(file.readlines())
log_lines.sort()
with open('summary.log','w') as f:
    f.writelines(log_lines)

# 388. Monitor folder for new files and move by extension
watch_folder = 'incoming'
for f in os.listdir(watch_folder):
    ext = f.split('.')[-1]
    os.makedirs(f"{watch_folder}/{ext}",exist_ok=True)
    shutil.move(os.path.join(watch_folder,f), f"{watch_folder}/{ext}/{f}")

# 389. Extract table from HTML and save as CSV
html = open('page.html').read()
rows = re.findall(r'<tr.*?>(.*?)</tr>', html, re.DOTALL)
with open('table.csv','w',newline='') as f:
    writer = csv.writer(f)
    for r in rows:
        cols = re.findall(r'<t[dh].*?>(.*?)</t[dh]>', r, re.DOTALL)
        writer.writerow([c.strip() for c in cols])

# 390. Subprocess automation: run command, log output
cmd = ['echo','Automation test']
with open('cmd.log','w') as f:
    subprocess.run(cmd, stdout=f)

# 391. Archive old files and log names
archive_folder = 'archive'
os.makedirs(archive_folder, exist_ok=True)
for f in os.listdir('data'):
    if os.path.getmtime(os.path.join('data',f)) < datetime.now().timestamp()-86400*7:
        shutil.move(os.path.join('data',f), archive_folder)
        with open('archive.log','a') as logf:
            logf.write(f"{f} moved at {datetime.now()}\n")

# 392. Parse multiple CSVs, calculate column sums
col_sums = {}
for f in os.listdir('csv_folder'):
    if f.endswith('.csv'):
        with open(os.path.join('csv_folder',f)) as file:
            reader = csv.DictReader(file)
            for row in reader:
                for k,v in row.items():
                    col_sums[k] = col_sums.get(k,0)+int(v)
print(col_sums)

# 393. Validate JSON files in folder
for f in os.listdir('json_folder'):
    if f.endswith('.json'):
        with open(os.path.join('json_folder',f)) as file:
            try:
                json.load(file)
            except:
                print(f"Invalid JSON: {f}")

# 394. Convert multiple JSONs to CSV
for f in os.listdir('json_folder'):
    if f.endswith('.json'):
        with open(os.path.join('json_folder',f)) as file:
            data = json.load(file)
        if data:
            with open(f"{f.rsplit('.',1)[0]}.csv",'w',newline='') as out:
                writer = csv.DictWriter(out,fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)

# 395. Combine log filtering, parsing, and backup
filtered_logs=[]
for f in os.listdir('logs'):
    if f.endswith('.log'):
        with open(os.path.join('logs',f)) as file:
            for line in file:
                if 'ERROR' in line or 'WARN' in line:
                    filtered_logs.append(line.strip())
with open('filtered.log','w') as out:
    out.write('\n'.join(filtered_logs))
shutil.copy('filtered.log', f"backup/filtered_{datetime.now().strftime('%Y%m%d')}.log")

# 396. Monitor folder and execute a command when new file appears
new_files = set(os.listdir('watch_folder'))
time.sleep(2)
current_files = set(os.listdir('watch_folder'))
added = current_files-new_files
if added:
    for f in added:
        subprocess.run(['echo', f"New file detected: {f}"])

# 397. Parse HTML files, extract headings and save to JSON
headings=[]
for f in os.listdir('htmls'):
    html = open(os.path.join('htmls',f)).read()
    h = re.findall(r'<h[1-6].*?>(.*?)</h[1-6]>', html)
    headings.append({f:h})
with open('headings.json','w') as out:
    json.dump(headings,out,indent=2)

# 398. Aggregate numeric data from multiple CSVs and email summary (skeleton)
totals={}
for f in os.listdir('csv_folder'):
    if f.endswith('.csv'):
        with open(os.path.join('csv_folder',f)) as file:
            reader = csv.DictReader(file)
            for row in reader:
                for k,v in row.items():
                    totals[k] = totals.get(k,0)+int(v)
print("Aggregated totals:", totals)
# Send via email using EmailMessage

# 399. Rename files based on content regex match
pattern = re.compile(r'DATE(\d{8})')
for f in os.listdir('texts'):
    with open(os.path.join('texts',f)) as file:
        content = file.read()
        match = pattern.search(content)
        if match:
            os.rename(os.path.join('texts',f), os.path.join('texts', f"{match.group(1)}_{f}"))

# 400. Full mini-project: fetch logs, parse errors, backup, and summarize
summary=[]
for f in os.listdir('logs'):
    if f.endswith('.log'):
        with open(os.path.join('logs',f)) as file:
            errors = [line.strip() for line in file if 'ERROR' in line]
            if errors:
                summary.append({'file':f,'errors':len(errors)})
                shutil.copy(os.path.join('logs',f), f"backup/{f}")
with open('summary.json','w') as out:
    json.dump(summary,out,indent=2)
print("Mini automation project completed. Summary saved.")