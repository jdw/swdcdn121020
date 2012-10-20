import sys
from BeautifulSoup import BeautifulSoup as Soup


def main():
    file = "/home/jdw/src/swdcdn121020/assets/source.html"
    handler = open(file).read()
    soup = Soup(handler)
    print soup.find("th", {"id": "system_name"}).text


if __name__ == "__main__":
    main()
