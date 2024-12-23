import re
from collections import Counter

#open and load text1 and text2
def load_inputs(first_input, second_input):
    
    if isinstance(first_input, str):
        try:
            with open(first_input, "r") as file1:
                text1 = file1.read()
        except FileNotFoundError:
                text1 = first_input
    else:
        raise TypeError("Please provide string or file as first parameter")

    if isinstance(second_input, str):
        try:
            with open(second_input, "r") as file2:
                text2 = file2.read()
        except FileNotFoundError:
                text2 = second_input
    else:
        raise TypeError("Please provide string or file as first parameter")
    
    return text1, text2

def convert_to_list(text_one, text_two):
    similarities_list1 = []
    similarities_list2 = []
    words_1 = text_one.split()
    words_2 = text_two.split()
    similarities_list1.extend(words_1)#add text into list
    similarities_list2.extend(words_2)#add text into list
    
    return similarities_list1, similarities_list2

def compare_and_find(filepath, input_1, input_2):
    try:
        from stop_words import stop_words
                      
    except ImportError:
        raise TypeError("File 'stop_words.py' has not been found")
    #spot words string into list
    
    
    filtered_speech1 = [word for word in input_1 if word not in stop_words]
    filtered_speech2 = [word for word in input_2 if word not in stop_words]
    
    
    #return filtered_speech1, filtered_speech2
    #last touch to find similarities in filtered speech1 and 2
    similar_list = []

    for word in filtered_speech1:
        if word in filtered_speech2:
            similar_list.append(word)

    return similar_list

    
def main():
    #load the file or texts
    speech1, speech2 = load_inputs("michelle_obama_speech.txt", "melina_trump_speech.txt")
    
    
    #convert to lists
    list1, list2 = convert_to_list(speech1, speech2)
    
    
    #open stop words, and list1, list2    
    magic = compare_and_find("stop_words.py", list1, list2)
    
    print(magic)
    

if __name__ == "__main__":
    main()