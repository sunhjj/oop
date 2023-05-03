import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=python&tbm=isch&ved=2ahUKEwjR7K3x19j-AhV6U_UHHeUTAq8Q2-cCegQIABAA&oq=python&gs_lcp=CgNpbWcQAzIECCMQJzIECCMQJzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEUABYAGDJEGgAcAB4AIABdIgBdJIBAzAuMZgBAKoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=VxVSZJHlMvqm1e8P5aeI-Ao&bih=854&biw=1504&hl=ko"
userAgent = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
response = requests.get(url, headers=userAgent)
with open('yt.html', 'wt') as f:
  f.write(response.text)
with open('yt.html', 'rt') as f:
  soup = BeautifulSoup(f, "html.parser")
  imgs = soup.find_all('img') #, attrs={'data-src'})
  # print(len(imgs))
  tot = 0
  for img in imgs:
    try:
      # print(img['data-src'])
      res = requests.get(img['data-src'])
      if res:
        tot += 1
        with open(f'result_{tot}.jpg', 'wb') as f:
          f.write(res.content)
    except: continue
    
  print(tot)
      # print(img['src'])
    
    
# thumbnails = soup.select("a > #thumbnail > img")

# for thumbnail in thumbnails:
#     print(thumbnail["src"])
