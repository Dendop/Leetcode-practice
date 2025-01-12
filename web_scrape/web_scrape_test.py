import requests
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    url = "http://olympus.realpython.org/profiles/dionysus"
    page = urlopen(url)

    html = page.read().decode("utf-8")
    name_start_index = html.find("Name:") + len("<h2>") + 2
    name_end_index = html.find("</h2>")
    name = html[name_start_index : name_end_index]

    fav_start_index = html.find("Favorite Color: ")
    fav_end_index = html.find("</center>")
    fav = html[fav_end_index - 5 : fav_end_index]
    
    print(name)
    print(fav)
    #print(html)
    
if __name__ == "__main__":
    main()