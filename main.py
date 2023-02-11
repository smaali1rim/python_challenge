from bs4 import BeautifulSoup
import requests
import csv
article = []

for i in range(1, 5):
    print (i)
    #make request to the website
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
    #parse html content of the page
    try:
        soup = BeautifulSoup(response.content, "lxml")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while parsing the response: {e}")
    list = soup.find('ol')
    books = list.find_all('article', class_="product_pod")
    #extract the elements
    for book in books:
        image = book.find('img')
        titles = image.attrs['alt']
        stars = book.find('p')['class'][1]
        prices = book.find('p', class_='price_color').text[1:]
        article.append([titles, stars, prices])
try:
    # Store the extracted information in a CSV file
    with open("articles.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Stars", "Price"])
        for article_data in article:
            writer.writerow(article_data)
except Exception as e:
    print(f"An error occurred while writing the CSV file: {e}")





