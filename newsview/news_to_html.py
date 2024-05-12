from newsview import NewsConfig, NewsLoader

class NewsToHtml:
  def __init__(self):
    self.html_top = '''
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
          <h1>South Korea</h1>      
        </div>
      </div>
      <div class="articles container">'''
      
    self.html_bottom = '''
      </div>  <!-- articles -->
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    </body>
    </html>
    '''
    
    self.html_mid = ''

  def add_article(self, image_url, url, title, desc, author, date):
    self.html_mid += f'''
                      <div class="article">
                        
                        <div class="news_image">
                          <img src="{image_url}" alt="">
                        </div> <!-- news_image -->

                        <div class="news_block">
                          <div class="news_title"><a href="{url}">{title}</a></div>
                          <div class="news_desc">{desc}</div>
                          <div class="news_author">{author}</div>
                          <div class="news_date">{date}</div>    
                        </div>  <!-- news_block -->

                      </div>  <!-- article -->
                  '''
                  
  def save(self, filename):
    with open(filename, 'w') as f:
      f.write(self.html_top)
      f.write(self.html_mid)
      f.write(self.html_bottom)
      
      
if __name__ == "__main__":
  conf = NewsConfig('config.json')
  news_loader = NewsLoader()
  news_loader.load_news(conf.get_base_url(), 
                        conf.get_api_key(), 
                        conf.get_lang_code(0), 
                        conf.get_category(0))
  
  news_html = NewsToHtml()
  for article in news_loader.articles:
    news_html.add_article(article['urlToImage'], 
                          article['url'], 
                          article['title'], 
                          article['description'], 
                          article['author'], 
                          article['publishedAt'])
    
  news_html.save('korea_news.html')