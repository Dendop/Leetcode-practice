import re
from collections import Counter

def find_most_common_words(user_input, n):
    
    if n <= 0:
        raise ValueError("The number must be positive and can't be zero")
    
    if isinstance(user_input, str):
        try:
            with open(user_input, "r") as file:
                text = file.read()
        except FileNotFoundError:
            text = user_input
          
    else:
        raise TypeError("The first parameter must be string or file")
    
    words = re.findall(r"\b\w+\b", text.lower())
    
    word_counts = Counter(words)
    
    return word_counts.most_common(n)

def main():
    magic = find_most_common_words("donald_speech.txt", 5)
    print(magic)





if __name__ == "__main__":
    main()