'''
Real world example: multithreading for i/o tasks
Scenario:Web Scraping

Web scarping involves making numerous network requests to fetcg web pages . These tasks are I/O bound because they spend a lot of time waiting for responses from server. multithreading can significantly improve the performance by allowing multiple web pages to be fetched concurrently.
'''

import threading
import requests
from bs4 import BeautifulSoup

urls=[
  'https://python.langchain.com/v0.2/docs/introduction/',
  'https://python.langchain.com/v0.2/docs/concepts/',
  'https://python.langchain.com/v0.2/docs/tutorials/'
]

def fetch_content(url):
  response=requests.get(url)
  soup=BeautifulSoup(response.content,'html.parser')
  print(f'fetched {len(soup.text)} characters from {url}')


threads=[]

for url in urls:
  thread=threading.Thread(target=fetch_content,args=(url,))
  threads.append(thread)
  thread.start()

for thread in threads:
  thread.join()

print("all web pages fetched")



