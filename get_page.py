#!/usr/bin/python3

from requests_html import HTMLSession
from urllib.parse import urlencode
import pprint
from bs4 import BeautifulSoup


API_KEY= "ADD KEY HERE"

def get_scrapeops_url(url):
    payload = {
        "api_key": API_KEY,
        "url": url
    }
    proxy_url = "https://proxy.scrapeops.io/v1/?" + urlencode(payload)
    return proxy_url

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
session = HTMLSession()
r = session.get(get_scrapeops_url('https://indeed.com/jobs?q=cybersecurity&l=33966'))
r.html.render()
soup = BeautifulSoup(r.html.html)
f = open('out.txt','w')
f.write(soup.prettify())
f.close()
