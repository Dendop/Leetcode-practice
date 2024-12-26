import requests
import json
import re
from collections import Counter
from bs4 import BeautifulSoup

def main():
    url_link = "https://www.gutenberg.org/cache/epub/1513/pg1513-images.html"
    response = requests.get(url_link)

    url_text = response.text
    
    soup = BeautifulSoup(url_text, "html.parser")
    cleaned_text = soup.get_text()

    word = re.findall(r"\b\w+\b", cleaned_text)

    words_count = Counter(word)
    find = words_count.most_common(10)

    print(find)
    
    




if __name__ == "__main__":
    main()