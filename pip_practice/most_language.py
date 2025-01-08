import requests
from collections import Counter, defaultdict
import json

def main():
    country_link = "https://restcountries.com/v3.1/all"
    response = requests.get(country_link)
    
    country_data = response.json()
    
    all_languages = []
    
    for lang in country_data:
        
        language = lang.get('languages', {})
        

        all_languages.extend(language.values())
    magic = Counter(all_languages)
    print(magic.most_common(10))

if __name__ == "__main__":
    main()