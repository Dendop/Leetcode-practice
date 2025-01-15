from bs4 import BeautifulSoup
import requests

def main():
    url = "https://www.scrapethissite.com/pages/simple/"
    response = requests.get(url)

    page = response.text
    soup = BeautifulSoup(page, "html.parser")
    print(soup)

if __name__ == "__main__":
    main()