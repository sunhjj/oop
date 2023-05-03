import requests, json
import pandas as pd
from bs4 import BeautifulSoup




class UrlHandler:
  url_is_empty:str = "URL is empty"
  
  def __init__(self) -> None:
    self.__url = None    
    
  def returnJson(self, content:bytes):
    jsonData = None
    try:
      jsonData = json.loads(content)      
    except TypeError as e:
      print(f"TypeError : {str(e)}")
    except:
      print(f"UrlHandler::requestJson() ===> 알 수 없는 에러가 발생하였습니다")
    finally:
      return jsonData
    
  def request(self, url:str, isHtml:bool=True):
    if url is None:      
      return UrlHandler.url_is_empty
    
    res = requests.get(url)
    if res.status_code == 200:      
      self.__url = url
      return res.content if isHtml else self.returnJson(res.content)
      
      
      
class CheckIterable:
  """아주 초간단한 Iterable한 객체인지 체크하는 클래스"""
  def isIterable(self, obj:object) -> bool:    
    """Iterable한 객체이면 True를 아니면 False를 반환"""
    try:
      iterable = iter(obj)
    except TypeError as e:
      return False
    except:
      return False
    
    return True



class StockInfoGetter(UrlHandler, CheckIterable):
  def __init__(self) -> None:
    super().__init__()    
    
  def init(self):
    url = "https://finance.naver.com/sise/sise_market_sum.naver"
    res = self.request(url)
    self._parseHtml(res)
  
  def update(self):
    self.init(self)
    
  def _parseHtml(self, htmlData):
    bs = BeautifulSoup(htmlData, 'html.parser')    
    table = bs.find('table', {'class':'type_2'})
    if not self.isIterable(table):
      return
    
    
    
    self.liHead = [item for item in table.thead.text.split('\n') if item ]    
    
    litr = list()
    trs = table.tbody.find_all('tr')
    for tr in trs:
      # tds = tr.find_all('td', class_='blank_08')
      # if len(tds) > 0: 
      #   continue
      
      tds = tr.find_all('td', class_=['blank_09', 'blank_06', 'blank_08', 'division_line', 'division_line_1'])
      if len(tds) > 0: 
        continue
      
      # tds = tr.find_all('td', class_='blank_06')
      # if len(tds) > 0: 
      #   continue
      
      # tds = tr.find_all('td', class_='division_line')
      # if len(tds) > 0: 
      #   continue
      
      # tds = tr.find_all('td', class_='division_line_1')
      # if len(tds) > 0: 
      #   continue
      
      tds = tr.find_all('td')      
      li = list()
      for td in tds:
        a = td.find_all('a', class_="title")
        if a:
          li.append(a.text.strip())
        else:
          li.append( int(td.text.strip()) if td.text.strip().isnumeric() else td.text.strip() )
          
          
      if len(li):
        litr.append(li)
    
    # print(litr)
    litr = [item for item in litr if len(item)]     
    self.df = pd.DataFrame(litr, index=None, columns=self.liHead) #, columns=self.liHead)
    # print(self.df)
  

sGetter = StockInfoGetter()
res = sGetter.init()
sGetter.df.to_excel('output.xlsx', index=False)
# print(sGetter.df.loc[[0,2]])
# print(sGetter.df.info())
# if res is not None:
#   print(res)
# else:
#   print("URL 요청(Request) 실패!!!")

