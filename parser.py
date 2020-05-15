from user_agent import generate_user_agent
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
page_response = requests.get('https://www.ozon.ru/category/ortopedicheskie-podushki-31148/', timeout=5, headers=headers)

print(page_response.text)