from bs4 import BeautifulSoup
import requests

class MyScrapper:
  def __init__(self, url):
    try:
      res = requests.get(url)
      if res.status_code != 200:
        raise Exception(f'Error: Unable to load {url}')      
      self.soup = BeautifulSoup(res.content, 'html.parser')
    except Exception as e:
      print(f'Error: {e}')
      raise Exception(f'Error: {e}')
    
  def get_title(self):
    try:
      return self.soup.title.string
    except Exception as e:
      print(f'Error: {e}')
      raise Exception(f'Error: {e}')
    
  def get_first_div(self):
    try:      
      content = self.soup.body.div.contents
      attrs = self.soup.body.div.attrs
      return (content, attrs)
    except Exception as e:
      print(f'Error: {e}')
      raise Exception(f'Error: {e}')
    
  def get_news_container(self):
    try:
      return self.soup.find('div', {'name': 'NewsContainer'})
    except Exception as e:
      print(f'Error: {e}')
      raise Exception(f'Error: {e}')
    
    

if __name__ == "__main__":
  scrapper = MyScrapper('http://127.0.0.1:5500/newsview/kr_health_20240520_025343.html')
  # print(scrapper.get_title())
  # print()
  # print(type(scrapper.get_first_div()))
  # print()
  # print(scrapper.get_first_div())
  # print()
  # for i, content in enumerate(scrapper.get_first_div()):
  #   print(i+1)
    
  # print()
  # # 리스트에서 '\n'을 제거하고 출력
  # li = [x for x in scrapper.get_first_div() if x != '\n']
  # print(li, len(li))
  
  
  news_container = scrapper.get_news_container()
  for content in news_container.children:
    if content.name == 'div':
      print(content.attrs)
      print(content.contents)
      print()