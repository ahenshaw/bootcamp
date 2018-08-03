''' scrape_html2 - Begin to parse the HTML'''

# third-party libraries
import requests
from bs4 import BeautifulSoup
import custom

url = 'http://graduate.kennesaw.edu/datascience/students.php'

# retrieve web page and parse
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
# print(soup)

# find the relevant blocks of HTML
info_blocks = soup.findAll('div', {'class':'more_info'})
print(len(info_blocks))

