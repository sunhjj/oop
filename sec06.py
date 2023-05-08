import requests, json
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from bs4 import BeautifulSoup





class UrlHandler:
  url_is_empty:str = "URL is empty"
  
  def __init__(self) -> None:
    super().__init__()
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
    
  def request(self, url:str, userAgent:str=None, isHtml:bool=True):
    if url is None:      
      return UrlHandler.url_is_empty
    #cookie = 'YSC=WUySKZimQq8; VISITOR_INFO1_LIVE=p0u6E9FfurQ; DEVICE_INFO=ChxOekU0TmprNE5qazVNVFUzTWpZME5EQXdPQT09EJed9Z0GGJed9Z0G; HSID=A7hoP1eji1YxhCt11; SSID=A2WGeNgGFOQ0eipjD; APISID=llttYuxDJ9Oicl7B/AdDBy_sf4-UL0yIQd; SAPISID=-lemmwRXAPzgunZk/AvNSRQ4E-9joeYhKV; __Secure-1PAPISID=-lemmwRXAPzgunZk/AvNSRQ4E-9joeYhKV; __Secure-3PAPISID=-lemmwRXAPzgunZk/AvNSRQ4E-9joeYhKV; PREF=f6=80080&f7=100&tz=Asia.Seoul&f3=8&f4=4000000&f5=30000; SID=Vwg09D8XmS7hM1utxtfsCu2d5Bvh9xK_02aZrjWfMz5sKk_QK29R1O8ej688ErLIRvgWAw.; __Secure-1PSID=Vwg09D8XmS7hM1utxtfsCu2d5Bvh9xK_02aZrjWfMz5sKk_QTnd6-PPwzyG9UeCupBNHnw.; wide=1; LOGIN_INFO=AFmmF2swRQIhAJPHkuKIhj8C9wWTP_InT-7u_yeq1t5G1AJ01cilpgLXAiBocg2epX67JVSUbsTKojU1jFOYtZGKu7i0ZmkV0_VslQ:QUQ3MjNmd1h3eFFLbGJVZVp1UkNLUlFGRmFWei1nRWVPNWx0OV9CMzBUUUxMOWZLUU1YUTlNOVZZQ0Izd3JGcGR0djhTalQ2bVNpVmsyQWduS1p5UHJuNFJ1TDBTYS1sMGh3ckwzM0lmME1wX19aNlR0SEE0WEFBYkF1bVBielg3NmdzNkhBTk1jOUpGRlhDNWd3alpDdmQyZGNYSXQzQm5R; __Secure-3PSID=Vwg09D8XmS7hM1utxtfsCu2d5Bvh9xK_02aZrjWfMz5sKk_QfNp18-HKyQGwHvro82kc4A.; SIDCC=AP8dLtxbjxNyuwOcV6BBTtudMc_HZu9AWK8CutikWgFRiDzGmlCh8o6kec-_xEeIVF7PTl8nOSY; __Secure-1PSIDCC=AP8dLtwUXeVqpc2OE5__d5perfPlSRDZIXxE7J3cZB5-FJO2AIlECUE2XRcmAEuXswtGq8COhBw; __Secure-3PSIDCC=AP8dLtwlPv-vHnfbTzT74QvkfsffFUyqhxJnfFakJ6sb75K01yJ3Tk8kGTANEueMCplfojDo8t8'
    header = {'User-Agent': userAgent} #, 'cookie':cookie}
    res = requests.get(url, headers=header)
    if res.status_code == 200:      
      self.__url = url
      return res.content if isHtml else self.returnJson(res.content)
      
      
      
class CheckIterable:
  def __init__(self) -> None:
    super().__init__()
    
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
    
  def convertToNumeric(self, val:str) -> any:
    val = val.replace(',', '')
    val = val.replace('%', '')
    val = val.replace('N/A', '0')
    try:
      return int(val)
    except ValueError:
      try:
        return float(val)
      except ValueError:
        return val
    
  def updateToNumeric(self, liStr:list) -> any:
    if not self.isIterable(liStr):
      return liStr
    
    retLi = []
    for item in liStr:
      retLi.append(self.convertToNumeric(item))
      
    return retLi
    
  def _parseHtml(self, htmlData):
    bs = BeautifulSoup(htmlData, 'html.parser')    
    table = bs.find('table', {'class':'type_2'})
    if not self.isIterable(table):
      return
    
    self.liHead = [item for item in table.thead.text.split('\n') if item ]    
    
    litr = list()
    trs = table.tbody.find_all('tr', attrs={'onmouseover':True})
    for tr in trs:
      # tds = tr.find_all('td', class_=['blank_09', 'blank_06', 'blank_08', 'division_line', 'division_line_1'])
      # if len(tds) > 0: 
      #   continue
      
      # tds = tr.find_all('td', class_='blank_08')
      # if len(tds) > 0: 
      #   continue
      
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
          li.append( self.convertToNumeric(td.text.strip()) )
                    
                    # int(td.text.strip()) if td.text.strip().isnumeric() else td.text.strip() )
      if len(li):
        litr.append(li)
    
    # print(litr)
    litr = [item for item in litr if len(item)]     
    self.df = pd.DataFrame(litr, index=None, columns=self.liHead) #, columns=self.liHead)
    # print(self.df)
  
  
fp = fm.FontProperties(family=['AppleGothic'], size=12)

sGetter = StockInfoGetter()
res = sGetter.init()
df = sGetter.df
df.loc[df['등락률']<0, '전일비'] = -df['전일비']
df.to_excel('output.xlsx', index=False)
df = df.reset_index(drop=True)
df.drop('N', axis=1, inplace=True)
df.drop('토론실', axis=1, inplace=True)
df = df.set_index('종목명')
print(df.info())
df.corr().to_excel('parse.xlsx')
# print(df.to_string())
df.plot()

print(mpl.rcParams['font.family']) # font
print(mpl.rcParams['font.size']) # size

plt.rcParams['font.family'] = 'AppleGothic'
mpl.rcParams['axes.unicode_minus'] = False
plt.show()

# print(df.corr())
# print(sGetter.df.loc[[0,2]])
# print(sGetter.df.info())
