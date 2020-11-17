# baka-scraper
Scrapy spider to scrape from Baka Updates

## Install Scrapy
```
pip install scrapy
```

## Run the Spider
1. Change the base URL in `spiders/baka_spider.py` to whatever main page you want to scrape from. This should be a page that contains direct links to series. For example, for Yen Press, use the below:

```
start_urls = ['https://www.mangaupdates.com/publishers.html?id=279']
```

2. In the main directory, run the following command:

```
scrapy crawl baka_spider
```

3. If you would like to dump the results into a CSV file, run

```
scrapy crawl baka_spider >> myfilename.csv
```

Voila! You've scraped some data :) 
