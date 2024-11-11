import json


def most_populated_countries(file_dct, n):
    
    top_countries = sorted(
        file_dct,
        key=lambda country: country.get("population", 0),
        reverse=True
    )[:n]
    return top_countries

def main():
    with open("countries_data.json", "r", encoding="utf-8") as js_file:
        file_dct = json.load(js_file)
        
    
    magic  = most_populated_countries(file_dct, 2)
    for country in magic:
        print(f"Country : {country["name"]}, population: {country["population"]}")


if __name__ == "__main__":
    main()