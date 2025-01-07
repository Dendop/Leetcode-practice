import requests
from collections import Counter
from collections import defaultdict
import json

def main():
    countries_link = "https://restcountries.com/v3.1/all"
    response = requests.get(countries_link)
    
    countries_with_population = defaultdict(list)
    
    if response.status_code != 200:
        print("The API data could not be fetched")
    
    countries_data = response.json()
    
    for pop in countries_data:
        name = pop.get('name', {}).get('common', 'Unknown')
        population = pop.get('population', 0)
        countries_with_population[name].append(population)
        
    magic = Counter(countries_with_population)
    print(magic.most_common(10))
    


if __name__ == "__main__":
    main()