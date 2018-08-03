''' scrape_html1 - Exploration'''

# third-party libraries
import requests

url = 'http://graduate.kennesaw.edu/datascience/students.php'

response = requests.get(url)
print(response.content)