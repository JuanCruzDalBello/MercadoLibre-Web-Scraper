# MercadoLibre-Web-Scraper
Web Scraping script for https://www.mercadolibre.com.ar/

# Usage
Download repository.

In terminal:

    $ python web_scraper.py

Upon execution, the user is asked for a searching term (i.e. bike, old books, 80s retro paintings, etc...) and the amount of pages he wants the script to look into.

    $ Searching term: string

    $ Amount of pages: integer

After givin a searching term and the amount of pages, the script opens a Google Chrome instance and starts searching for the article, through the indicated number of pages.

Once the script stops, inside the same directory, the file 'MercadoLibre_reslts.csv' is created, which contains the data of every item listed.

The data consists of the name of the item, its price, amount of reviews and URL.
