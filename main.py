from requests import get

r = get("https://www.goodreads.com/choiceawards/best-fantasy-books-2021")
print(r.status_code)