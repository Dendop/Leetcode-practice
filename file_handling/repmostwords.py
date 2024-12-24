from collections import Counter
import re

def main():
    lines = []
    try:
        with open("romeo_and_juliet.txt", "r") as file:
            for line in file:
                lines.extend(line.split())


    except FileNotFoundError:
        raise TypeError("File has not been found")

    finder = Counter(lines)
    new_list = finder.most_common(10)
    print(new_list)
    
if __name__ == "__main__":
    main()