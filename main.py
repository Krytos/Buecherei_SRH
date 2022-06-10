from requests import get
from bs4 import BeautifulSoup

URL = "https://www.goodreads.com"
r = get(URL)

soup = BeautifulSoup(r.content, "html.parser")
result = soup.find_all("a", class_="gr-hyperlink")

link1 = []
link2 = []

for best_books in result:
    spl = best_books["href"].split("/")
    if spl[1] == "genres":
        URL2 = URL + str(best_books["href"])
        print("URL2: " + URL2)
        r2 = get(URL2)
        soup2 = BeautifulSoup(r2.content, "html.parser")
        divs = soup2.find_all("div", class_="coverWrapper")
        for books in divs:
            URL3 = URL + str(books.find("a")["href"])
            print("URL3: " + URL3)
            link2.append(URL3)
        #print(link2)