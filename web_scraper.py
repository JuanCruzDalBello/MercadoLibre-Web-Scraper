import csv
from bs4 import BeautifulSoup
from selenium import webdriver

# Chrome
from webdriver_manager.chrome import ChromeDriverManager


def get_url(term):
    """Generates a MercadoLibre url from a search term"""
    
    term = term.replace(' ', '-')

    # URL = MercadoLibre base listing url + searching term + index
    url = "https://listado.mercadolibre.com.ar/" + term + "_Desde_{}_NoIndex_True"

    return url


def extract_record(item):
    """Get specific data from the item"""
    # data -> (name, price, amount of reviews, url)

    # Name
    name = item.find("h2", {"class" : "ui-search-item__title"}).text

    # Price
    price = item.find("span", {"class" : "price-tag-fraction"}).text
    price = price.replace('.', ',')

    # Amount of reviews
    try:
        amount_of_reviews = item.find("span", {"class" : "ui-search-reviews__amount"}).text
    except AttributeError:
        amount_of_reviews = None
    
    # URL
    a_tag = item.a
    a_tag.text.strip()
    url = a_tag.get("href")

    results = (name, price, amount_of_reviews, url)    

    return results


def main():
    search_term = input("Search term: ")

    # Install chrome driver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # List to store all items data
    records = []

    # URL to start searching
    url = get_url(search_term)

    # Iterate through multiple pages on MercadoLibre
    for page in range(1, 302, 50):
        # Open web browser
        driver.get(url.format(page))

        # Extract a collection from current page
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Save items on the page that share a feature
        results = soup.find_all("div", {"class": "ui-search-result__wrapper"})

        # Extract wanted data from every item
        for item in results:
            record = extract_record(item)
            records.append(record)

    # Close web browser
    driver.close()

    # Save results into a csv
    with open("MercadoLibre_reslts.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Price", "Amount of reviews", "URL"])
        writer.writerows(records)


if __name__ == "__main__":
    main()