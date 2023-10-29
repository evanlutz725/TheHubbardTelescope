import requests
from pathlib import Path
from bs4 import BeautifulSoup
import re

response = requests.get(
  url='https://proxy.scrapeops.io/v1/',
  params={
      'api_key': Path('./scrapeops-apikey.txt').read_text(),
      'url': 'https://www.indeed.com/m/jobs?q=cybersecurity', 
  }
)

f = open('out.txt','w')
f.write(response.text)
f.close()

if(response.status_code != 200):
  print('request failed')
  exit(response.status_code)

soup = BeautifulSoup(response.text, 'lxml')
jobElements = soup.css.select('.jobsearch-JobCountAndSortPane-jobCount > span:first-child')

if (jobElements.count == 0):
  print('could not find job count')
  exit(1)
  
jobText = jobElements[0].get_text()
jobCount = int(re.match("(\d|,)+", jobText).group(0).replace(',', ''))
print(jobCount)