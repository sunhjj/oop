import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/"
response = requests.get(url)
with open('yt.html', 'wt') as f:
  f.write(response.text)
  
soup = BeautifulSoup(response.text, "html.parser")
thumbnails = soup.select("a > #thumbnail > img")

for thumbnail in thumbnails:
    print(thumbnail["src"])
