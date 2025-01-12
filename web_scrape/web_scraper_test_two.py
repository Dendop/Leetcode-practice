from bs4 import BeautifulSoup
import requests

def main():
    url_link = "http://olympus.realpython.org/profiles/dionysus"
    response = requests.get(url_link)

    if response.status_code != 200:
        raise Exception("url could not be reached")
    html = response.text
    
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    cleaned_text = ' '.join(text.split())
    image1, image2 = soup.find_all("img")
    print(image1)
    print(image2)
    #print(html)
    print(soup.title.string)
if __name__ == "__main__":
    main()