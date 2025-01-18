import requests
from bs4 import BeautifulSoup

def main():
    url = "http://olympus.realpython.org/profiles"
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    for link in soup.find_all("a"):
        link_url = url.strip('/profiles') + link["href"] #had to strip /profiles becasue of just .org is different page
        print(link_url)
    
if __name__ == "__main__":
    main()