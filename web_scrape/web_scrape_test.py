import requests
from bs4 import BeautifulSoup

def main():
    this_link = "https://archive.ics.uci.edu/ml/datasets.php"
    response = requests.get(this_link)
    
    print(response)


if __name__ == "__main__":
    main()