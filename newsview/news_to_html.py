from myutil import clear_screen
from newsview import NewsConfig, NewsLoader
import datetime

class NewsToHtml:
  def __init__(self, country_name='South Korea', category='topic'):
    self.html_top = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
      <link rel="stylesheet" href="style.css">
      <title>Document</title>
    </head>
    <body>
      <div class="country">
        <div>
          <img src="resources/kr.svg" alt="">
        </div>
        <div class="country_name">
          <h1>{country_name}</h1>
          <h3>{category}</h3>
        </div>
      </div>
      <div class="articles container" name="NewsContainer">'''
      
    self.html_bottom = '''
      </div>  <!-- articles -->
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    </body>
    </html>
    '''
    
    self.html_mid = ''

  def add_article(self, image_url, url, title, desc, author, date):
    self.html_mid += f'''
                      <div class="article" id="news_blcok">
                        
                        <div class="news_image" id="news_image">
                          <img src="{image_url}" alt="">
                        </div> <!-- news_image -->

                        <div class="news_block" id="news_text">
                          <div class="news_title" id="news_title"><a href="{url}">{title}</a></div>
                          <div class="news_desc" id="news_desc">{desc}</div>
                          <div class="news_author" id="news_author">{author}</div>
                          <div class="news_date" id="news_date">{date}</div>    
                        </div>  <!-- news_block -->

                      </div>  <!-- article -->
                  '''
                  
  def save(self, filename):
    try:
      with open(filename, 'w') as f:
        f.write(self.html_top)
        f.write(self.html_mid)
        f.write(self.html_bottom)
    except Exception as e:
      print(f'Error: {e}')
      raise Exception(f'Error: {e}')
      
      
if __name__ == "__main__":
  conf = NewsConfig('config.json')
  news_loader = NewsLoader()
  
  for i, lang in enumerate(conf.get_language()):
    print(f'{i+1} : {lang["code"]}, {lang["name"]}')
    
  sel = int(input('Select language: '))
  lang_code = conf.get_lang_code(sel-1)
  lang_name = conf.get_language()[sel-1]['name']
  
  clear_screen()
  
  for i, cat in enumerate(conf.get_categories()):
    print(f'{i+1} : {cat}')
    
  sel = int(input('Select category: '))
  category = conf.get_category(sel-1)
  
  clear_screen()
  
  news_loader.load_news(conf.get_base_url(), 
                        conf.get_api_key(), 
                        lang_code, 
                        category)
  
  news_html = NewsToHtml(lang_name, category)
  for article in news_loader.articles:
    news_html.add_article(article['urlToImage'], 
                          article['url'], 
                          article['title'], 
                          article['description'], 
                          article['author'], 
                          article['publishedAt'])
    
  now = datetime.datetime.now()
  current_datetime = now.strftime("%Y%m%d_%H%M%S")
  html_filename = f'{lang_code}_{category}_{current_datetime}.html'
  news_html.save(html_filename)
  
  print(f'HTML file saved as {html_filename}')