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
    print(f"Total number of all languages = {len(all_languages)}")
    no_dup = set(all_languages) #total number without duplicates
    print(f"Total number of languages = {len(no_dup)}")

if __name__ == "__main__":
    main()