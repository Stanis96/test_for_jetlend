import requests
from bs4 import BeautifulSoup


url = "https://jetlend.ru"


def get_all_tags(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    body = soup.find_all()
    tags = [tag.name for tag in body]
    tags_attrs = [tag for tag in body if len(tag.attrs) > 0]
    result = {"tags": len(tags), "tags_attrs": len(tags_attrs)}
    print(result)


if __name__ == "__main__":
    get_all_tags(url)
