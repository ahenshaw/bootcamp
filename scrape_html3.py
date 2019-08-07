''' scrape_html3 - Complete example'''

# third-party libraries
import requests
from bs4 import BeautifulSoup
import custom

URL = 'http://graduate.kennesaw.edu/datascience/students.php'

# retrieve web page and parse
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'lxml')

# find the relevant blocks of HTML
info_blocks = soup.findAll('div', {'class':'more_info'})

# then descend and extract
for info in info_blocks:
    title_div = info.find_previous_sibling('div')
    title = title_div.span.text.strip()
    print(title)
    
    for li in info.ul.findAll('li'):
        print(li.text.strip())
    print()
