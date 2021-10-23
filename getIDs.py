# Copyright © Fall 2021 Ivan Chen
# Liscensed under MIT License
# A CLI tool to submit homework to the StuyCS homework server
# Bugs? https://github.com/anivanchen/stuycs-submit/issues

import requests
from bs4 import BeautifulSoup

url = 'http://bert.stuy.edu/{}/{}/pages.py?page=submit_homework'.format(input('Teacher Name (ex. dholmes): '), input('Term (ex. fall2021): '))
page = requests.get(url)
substring = ''

soup = BeautifulSoup(page.content, 'html.parser')
script = soup.find('script').string.split(' ++i)', 1)[0].split(';')

for line in script: 
  if 'students[' in line:

    # find period
    start = line.find('"') + len('"')
    end = line.find('|')
    period = line[start:end]

    # find id
    start = line.find('|') + len('|')
    end = line.replace('|', '', 1).find('|')
    id = line[start:end+1]

    # find name
    start = line.replace('|', '', 1).find('|') + len('|')
    end = line.replace('"', '', 1).find('"')
    name = line[start+1:end+1]

    substring = substring + period + " '" + name + "': '" + id + "',\n"

file = open('IDs.txt', 'w')
file.write(substring)
file.close()