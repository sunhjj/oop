import requests, time
from bs4 import BeautifulSoup

start = time.time()

url = "https://www.google.com/search?q=korea&rlz=1C5CHFA_enKR1010KR1010&sxsrf=APwXEddiTIk2v25rMaUTASedf74K_d92qQ:1683176769403&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjYwryL8tr-AhXYEXAKHeeaCucQ_AUoAXoECAIQAw&biw=1504&bih=1556&dpr=2"
header = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
response = requests.get(url, headers={"User-Agent":header})

soup = BeautifulSoup(response.content, "html.parser")
imgs = soup.find_all('img', attrs={'data-src':True})

tot = 1
for img in imgs:
  try:
    # print(img['data-src'])
    res = requests.get(img['data-src'])
    if res.status_code==200:      
      with open(f'result_{tot}.jpg', 'wb') as f:
        f.write(res.content)
        tot += 1
  except: continue

end = time.time()
print(f'프로그램 종료 : {end-start}')  

      # print(img['src'])
    
    
# thumbnails = soup.select("a > #thumbnail > img")

# for thumbnail in thumbnails:
#     print(thumbnail["src"])
# class A():
#   def __init__(self):
#     super().__init__()
#     self.x = 1

# # parent class B
# class B():
#   def __init__(self):
#     super().__init__()
#     self.y = 2

# # parent class C
# class C():
#   def __init__(self):
#     self.z = 3

# # target class D
# class D(A, B, C):
#   def __init__(self):
#     super().__init__()

# d = D()
# print(vars(d))