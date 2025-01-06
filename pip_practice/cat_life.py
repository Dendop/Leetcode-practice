import requests
import json
import statistics

def main():
    cat_link = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(cat_link)

    cat_data = response.json()

    lifespan_dict = {}

    for life in cat_data:
        name = life.get('name', 'Unknown')
        life_span = life.get("life_span")

        try:
            life_range = list(map(float, life_span.split(' - ')))
            min_life = min(life_range)
            max_life = max(life_range)
            mean_life = sum(life_range) / len(life_range)
            median_life = statistics.median(life_range)

        except (ValueError, TypeError):
            min_life = max_life = mean_life = median_life = None
            print("Life-span data was not found")

        lifespan_dict[name] = {
            "min" : min_life,
            "max" : max_life,
            "mean" : mean_life,
            "median" : median_life
        }

        life_json = json.dumps(lifespan_dict, indent = 2)
        print(life_json)
        
        with open("life_json", "w") as file:
            file.write(life_json)

if __name__ == "__main__":
    main()