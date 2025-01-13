import mechanicalsoup

def main():
    browser = mechanicalsoup.Browser()

    url = "http://olympus.realpython.org/login"

    page = browser.get(url)
    print(page.soup)

if __name__ == "__main__":
    main()