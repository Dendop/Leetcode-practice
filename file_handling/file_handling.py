import json

#count number of lines and words
def main():
    f = open(r"obama_speech.txt")
    check = f.readlines()
    line_count = 0
    word_count = 0
    for line in check:
        line_count += 1
        words = line.split() #this split words into list, Hello, world -> ["Hello", "world"]
        
        word_count += len(words)
    print(f"Obama speech lines: {line_count}, words: {word_count}")
    f.close()
    
    a = open(r"michelle_obama_speech.txt")
    a_check = a.readlines()
    line_count = 0
    word_count = 0
    for _ in a_check:
        line_count += 1
        a_words = _.split()
        word_count += len(a_words)
    print(f"Michele speech lines: {line_count}, words: {word_count}")
    a.close()
    
    with open(r"donald_speech.txt") as b:
        b_check = b.readlines()
        line_count = 0
        word_count = 0
        for i in b_check:
            line_count += 1
            b_words = i.split()
            word_count += len(b_words)
        print(f"Donald Trump speech lines: {line_count}, words: {word_count}")
        
    with open(r"melina_trump_speech.txt") as c:
        c_check = c.readlines()
        line_count = 0
        word_count = 0
        for j in c_check:
            line_count += 1
            c_words = j.split()
            word_count += len(c_words)
        print(f"MelinaTrump speech lines: {line_count}, words: {word_count} ")




if __name__ == "__main__":
    main()