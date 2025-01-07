import requests
import json
from collections import defaultdict

def main():
    cat_link = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(cat_link)
    
    cat_data = response.json()
    
    breeds_by_country = defaultdict(list)
    
    for cat in cat_data:
        breed_name = cat.get('name', 'Unknown')
        country = cat.get('origin', 'Unknown')
        breeds_by_country[country].append(breed_name)
    
    
    for country, breed in breeds_by_country.items():
        print(f"{country}: ", {' , '.join(breed)})
    

    breeds_in_country = json.dumps(breeds_by_country, indent = 2)
    
    with open("breeds_in_country", "w") as file:
        file.write(breeds_in_country)


if __name__ == "__main__":
    main()