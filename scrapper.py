from requests import get
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self, url):
        self.url = url
        r = get(self.url)

        soup = BeautifulSoup(r.content, "html.parser")
        result = soup.find_all("a", class_="gr-hyperlink")

        link1 = []
        link2 = []

        for best_books in result:
            spl = best_books["href"].split("/")
            if spl[1] == "genres":
                url2 = self.url + str(best_books["href"])
                r2 = get(url2)
                soup2 = BeautifulSoup(r2.content, "html.parser")
                divs = soup2.find_all("div", class_="coverWrapper")
                for books in divs:
                    url3 = self.url + str(books.find("a")["href"])
                    link2.append(url3)