#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mechanize
from bs4 import BeautifulSoup
import csv
import re
import logging

logging.basicConfig(filename='./logs/request.log',level=logging.DEBUG)

browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)

url = 'http://www.facebook.com/'
browser.open(url)
browser.select_form(nr = 0)
browser.form['email'] = 'your_login'
browser.form['pass'] = 'your_password'
response = browser.submit()

req = response.read()
soup = BeautifulSoup(req, "html5lib")
tags = soup.findAll('script')

idArray = []
idArrayAux = []

for tag in tags:
    script = re.compile(r',list:\[(.*)],short')
    if script.search(str(tag)):
        ids = script.findall(str(tag))[0]
        idArrayAux = ids.replace('"','').split(',')

for user in idArrayAux:
    idArray.append(user[:-2])


def runFindFriends():
    count = 0
    with open('./files/names.csv',"w") as csvFile:
        print csvFile
        csvWritter = csv.writer(csvFile, delimiter=';', quoting=csv.QUOTE_ALL)
        csvWritter.writerow(['NOME','ID','URL', 'SEQUENCIA'])
        for user in idArray:
            count = count + 1
            try:
                req = browser.open(url+user).read()
                logging.info('Url chamada com sucesso: ' + url+user)
            except Exception as e:
                logging.info('Url com erro: ' + url+user)
                logging.error(e, exc_info=True)
                pass

            soup = BeautifulSoup(req, "html5lib")
            name = soup.find('title').text
            csvWritter.writerow([name.encode('utf-8'), user, (url+user), count])
            print [name.encode('utf-8'), user, (url+user), count]

if __name__ == '__main__':
    runner = runFindFriends()
