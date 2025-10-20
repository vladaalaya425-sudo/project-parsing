import requests
from bs4 import BeautifulSoup
from time import sleep
from random import uniform

rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
base_url = "https://books.toscrape.com/catalogue/"
total_pages = 51
top_books = []

def download(url):
    try:    
        resp = requests.get(url, stream=True)
        r = open("c:\\Users\\Lenovo\\Desktop\\Projects\\image\\" + url.split("/")[-1], "wb")
        for value in resp.iter_content(1024*1024):
            r.write(value)
        r.close()
    except requests.exceptions.RequestException as e:
        print(f"[Ошибка загрузки] {url}: {e}")
    except OSError as e:
        print(f"[Ошибка сохранения файла] {url}: {e}")

def get_url(base_url, page = 1):
    for i in range (1, page+1):
        url = f"{base_url}page-{i}.html"
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "lxml") #html parser
            data = soup.find_all("article", class_ = "product_pod")
            for i in data:
                yield base_url + i.find("a").get("href")
        except Exception as e:
            print(f"[Ошибка получения url] {url}: {e}")
    
def array():
    for card_url in get_url(base_url, 3):
        try:
            response = requests.get(card_url)
            response.encoding = "utf-8"
            soup = BeautifulSoup(response.text, "lxml") #html parser
            data = soup.find("div", class_ = "content")
            title = data.find("h1").text.strip()
            price = data.find("p", class_ = "price_color").text
            rating = rating_map[data.find("p", class_ = "star-rating")["class"][1]]
            desc_text = data.find("div", class_ = "sub-header")
            text = desc_text.find_next("p").text
            url_img = "https://books.toscrape.com/" + data.find("img").get("src")
            url = card_url
            download(url_img)
            if rating == 5 and len(top_books)<10:
                top_books.append({
                "title" : title,
                "price" : price,
                "rating" : rating,
                "text" : text,
                "url_img" : url_img,
                "url" : card_url
                })
            sleep (uniform(1,2))
            yield title, price, text, url_img, url
        except Exception as e:
            print(f"[Ошибка парсинга] {card_url}: {e}")
    
if __name__ == "__main__":
    for book in array():
        print(array) 







    


