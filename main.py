import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)

empire_web_page = response.text

soup = BeautifulSoup(empire_web_page,"html.parser")

all_title = [title.get_text(strip=True) for title in soup.find_all(name="h3", class_="title") if title.get_text(strip=True)]
all_title.reverse()

print(all_title)
with open("movie.txt", encoding="utf-8", mode="w") as file:
    for title in  all_title:
        file.write(f"{title}\n")