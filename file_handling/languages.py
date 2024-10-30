import json
from collections import Counter

def get_languages(language_dct, n):
    lang_list = []
    
    for country in language_dct:
        languages = country.get("languages", [])
        lang_list.extend(languages)
    lang_count = Counter(lang_list)
    return lang_count.most_common(n)
def main():
    with open("countries_data.json", "r", encoding="utf-8") as json_file:
        language_dct = json.load(json_file)
    
    #print(language_dct)   
    magic = get_languages(language_dct, 10)    
    print("[")
    for i, j in magic:
        print(f"({i}, \'{j}\'),")
    print("]")  







if __name__ == "__main__":
    main()