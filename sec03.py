'''
UrlHandler :
url을 입력하면 해당 url로부터 request하여 response를 받아오는 클래스
'''

import requests, json

class UrlHandler:
  def __init__(self) -> None:
    self.__url = None
    
  def request(self, url:str):
    res = requests.get(url)
    if res.status_code==200:
      content = json.loads(res.content)
      self.__url = url
      return content
    
    return None
    
class City(UrlHandler):
  def __init__(self, apikey:str=None) -> None:
    super().__init__()
    self.name = None
    self.lat = None
    self.lon = None
    self.apikey = apikey
    
  # def load(self, filePath:str) -> dict:
  #   with open(filePath, "rt") as jsonFile:
  #     dic = json.load(jsonFile)
  #   return dic
  
  # def save(self, filePath:str) -> None:
  #   with open(filePath, "wt") as jsonFile:
  #     json.dump(self.cities, jsonFile)
      
  def setCurrentCity(self, city:str, country:str="kr"):
    if self.apikey is None:
      return
    
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city},{country}&appid={self.apikey}'
    res = self.request(url)
    
    self.name = res[0]['local_names']['ko']
    self.lat = res[0]['lat']
    self.lon = res[0]['lon']
    # self.cities[self.current_city] = (self.current_lat, self.current_lon)
  
  def getGeoInfo(self) ->dict:
    return {self.name:{"lat":self.lat, "lon":self.lon}}
  
  def getApiKey(self) -> str:
    return self.apikey
  

class CurrentWeather(UrlHandler):
  def __init__(self, city:City, units:str="metric", lang:str="ko") -> None:
    super().__init__()
    self.url = f'https://api.openweathermap.org/data/2.5/weather?lat={city.lat}&lon={city.lon}&lang={lang}&units={units}&appid={city.getApiKey()}'
    res = self.request(self.url)
    # print(res)
    self.parseJson(res)
    # print(self.url)

  def parseJson(self, jsonData:dict):
    self.weather = jsonData['weather']
    self.base = jsonData['base']
    self.main = jsonData['main']
    # self.sea_level = jsonData['sea_level']
    # self.grnd_level = jsonData['grnd_level']
    self.visibility = jsonData['visibility']
    self.wind = jsonData['wind']
    self.clouds = jsonData['clouds']
    self.dt = jsonData['dt']
    self.sys = jsonData['sys']
    self.timezone = jsonData['timezone']
    self.id = jsonData['id']
    self.name = jsonData['name']
    self.cod = jsonData['cod']
    
# web = UrlHandler()
# dic = web.request("http://api.openweathermap.org/geo/1.0/direct?q=안양,kr&appid=555e77f38f5b28cf6481409e56f93ad4")
# print(dic)
# print(web.__url)

cities = []
weathers = []
dic = dict()

for i in range(5):
  cities.append(City("555e77f38f5b28cf6481409e56f93ad4"))

for city in cities:
  name = input("도시 이름을 입력하세요 >>> ")
  if name:
    city.setCurrentCity(name)
    weathers.append(CurrentWeather(city))

dic = dict(zip(cities, weathers))
for city in dic:
  print( city.name )
  print( dic[city].weather )
  print( dic[city].main )
  print()

# curWeather = CurrentWeather(city1)
# print(curWeather.weather[0])
# print(curWeather.main)
# print('날씨 : {}, {}'.format(curWeather.weather[0]['main'], curWeather.weather[0]['description']))
# print('기온: {}℃, 체감기온: {}℃, 최저: {}℃, 최고: {}℃, 기압:{}, 습도:{}%'.format(curWeather.main['temp'], curWeather.main['feels_like'], curWeather.main['temp_min'], curWeather.main['temp_max'], curWeather.main['pressure'], curWeather.main['humidity']))
