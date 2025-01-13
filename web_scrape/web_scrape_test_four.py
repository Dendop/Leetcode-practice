import mechanicalsoup

def main():
    #1
    browser  = mechanicalsoup.Browser()
    url = "http://olympus.realpython.org/login"
    login_page = browser.get(url)
    html_page = login_page.soup
    
    #2
    form = html_page.select("form")[0]
    form.select("input")[0]["value"] = "zeus"
    form.select("input")[1]["value"] = "ThunderDude"

    #3
    profiles_page = browser.submit(form, login_page.url)

    links = profiles_page.soup.select("a")
    base_url = "http://olympus.realpython.org"
    for link in links:
        address = base_url + link["href"]
        text = link.text
        print(f"{text}:{address}")
    
if __name__ == "__main__":
    main()