'''
python에서 thread 사용하기
class, requests, thread, BeutifulSoup, time, os
'''

from sec06 import UrlHandler
from bs4 import BeautifulSoup
import threading, time, os

class ThreadWrapper:
  thread_id = 1
  def __init__(self) -> None:    
    self.thread = None
    self.id = ThreadWrapper.thread_id
    ThreadWrapper.thread_id += 1
    
  def __str__(self) -> str:
    return f'ThreadWrapper(id={self.id})'
  
  def start(self) -> None:
    self.thread = threading.Thread(target=self.Run)
    self.thread.start()
  
  def Run(self) -> any: pass
  
class GoogleImageSearchParser(UrlHandler):
  def __init__(self) -> None:
    super().__init__()
    
  def searchImage(self) -> any:
    self.url = "https://www.google.com/search?q=korea&rlz=1C5CHFA_enKR1010KR1010&sxsrf=APwXEddiTIk2v25rMaUTASedf74K_d92qQ:1683176769403&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjYwryL8tr-AhXYEXAKHeeaCucQ_AUoAXoECAIQAw&biw=1504&bih=1556&dpr=2"
    self.header = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    
    try:
      res = self.request(self.url, userAgent=self.header)
      if res is None: return None
    except:
      print(f"GoogleImageSearchParser에서 Runtime Error가 발생함!!!")
      return None
        
    bs = BeautifulSoup(res, 'html.parser')
    img_tags = bs.find_all('img', attrs={'data-src':True})
    
    for img in img_tags:
      url = img['data-src']
      getter = GoogleImageGetter()
      getter.startToGetImage(url, self.header)      
      
    
    
class GoogleImageGetter(UrlHandler, ThreadWrapper):
  def __init__(self) -> None:
    super().__init__()
    # print(f'{self.id}')
    
  def startToGetImage(self, url:str, userAgent:str):
    self.url = url
    self.userAgent = userAgent
    self.start()
    
  def Run(self) -> any:
    try:
      res = self.request(self.url, self.userAgent)
    except:
      print("이미지 요청중 오류가 발생함")
      return 0
      
    if isinstance(res, bytes):
      written = 0
      try:
        file_name = f'result_{self.id}.jpg'
        with open(file_name, 'wb') as f:
          written = f.write(res)
      except:
        print("File에 쓰는중 오류가 발생함!!!")
      finally:
        return written
    
    return 0
    
start = time.time()    
sp = GoogleImageSearchParser()
sp.searchImage()
end = time.time()
print(f'프로그램 종료 : {end-start}')

