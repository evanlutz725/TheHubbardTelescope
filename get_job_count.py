import requests
from pathlib import Path
from bs4 import BeautifulSoup
import re

response = requests.get(
  url='https://proxy.scrapeops.io/v1/',
  params={
      'api_key': Path('./scrapeops-apikey.txt').read_text(),
      'url': 'https://indeed.com/jobs?q=cybersecurity&l=33966', 
  }
)

soup = BeautifulSoup(response.content)
jobText = soup.css.select('.jobsearch-JobCountAndSortPane-jobCount > span:first-child')[0].get_text()
jobCount = int(re.match("(\d|,)+", jobText).group(0))
print(jobCount)