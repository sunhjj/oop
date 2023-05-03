import requests, json, re, datetime
from bs4 import BeautifulSoup

from sec06 import UrlHandler


class YouTubeThumbnailGetter(UrlHandler):
  def __init__(self) -> None:
    super().__init__()
    
  def init(self):
    url = "https://www.google.com/search?q=python&sxsrf=APwXEdfrv_bQh1UPnxecMFeXNO_-SS48xQ:1683098187630&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj33OGszdj-AhVGMXAKHZ0TBvcQ_AUoAXoECAEQAw&biw=1504&bih=1556&dpr=2"
    header = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    
    # 정식 브라우징 요청은 헤더 정보가 동반되면 좋다, 헤더정보가 동반되지 않으면 서버가 응답을 하지 않을 수 있다!!!
    htmlData = self.request(url, userAgent=header)
    return self.__parseHtml(htmlData)
    
  def __parseHtml(self, htmlData):
    # with open('yt.html', 'wt') as f:
    #   f.write(str(htmlData))
      
    bs = BeautifulSoup(htmlData, 'html.parser')
    imgs = bs.find_all('img') #, attrs={'class':'rg_i Q4LuWd'})    
    for img in imgs:
      print(img.attrs)
      
      # try:
      #   img_url=img['src']
      # except:
      #   img_url=img['data-src']
      #   continue
      
      # res = self.request(img_url)
      # if res:
      #   now = datetime.datetime.now()
      #   with open('pyimg_'+now.strftime("%Y%m%d_%H%M%S")+'.jpg', "wb") as f:        
      #     f.write( res )
      
      
      

ytImgGetter = YouTubeThumbnailGetter()
ytImgGetter.init()
      
