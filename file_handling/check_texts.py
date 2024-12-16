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

def find_similarities(text_one, text_two):
    similarities_list1 = []
    similarities_list2 = []
    words_1 = text_one.split()
    words_2 = text_two.split()
    similarities_list1.extend(words_1)#add text into list
    similarities_list2.extend(words_2)#add text into list
    
    return similarities_list1, similarities_list2
    
def main():
    #load the file or texts
    speech1, speech2 = load_inputs("michelle_obama_speech.txt", "melina_trump_speech.txt")
    
    
    #compare, find similarities
    list1, list2 = find_similarities(speech1, speech2)
    

if __name__ == "__main__":
    main()