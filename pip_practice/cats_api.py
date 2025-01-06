import requests
import statistics
import json


def main():
    cat_url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(cat_url)

    cat_data = response.json()
    
    breeds_weight = {}

    for cat in cat_data:
        name = cat.get('name', 'Unknown')
        weight_numeric = cat.get("weight", {}).get('metric', '')

        try:
            weight_range = list(map(float, weight_numeric.split(' - ')))
            min_weight = min(weight_range)
            max_weight = max(weight_range)
            mean_weight = sum(weight_range) / len(weight_range)
            median_weight = statistics.median(weight_range)

        except (ValueError, TypeError):
            min_weight = max_weight = mean_weight = median_weight = None

        breeds_weight[name] = {
            'min': min_weight,
            'max': max_weight,
            'mean': mean_weight,
            'median' : median_weight
        }
        #convert dict into json string
        cats_weight_json = json.dumps(breeds_weight, indent = 2)

        print(cats_weight_json)

        #save into JSON file
        with open("cats_weight_json", "w") as file:
            file.write(cats_weight_json)

if __name__ == "__main__":
    main()