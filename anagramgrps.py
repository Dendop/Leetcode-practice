def main():
    strs = ["act","pots","tops","cat","stop","hat"]
    anagrams = {}
    
    for word in strs:
        #sort the words
        sorted_word = ''.join(sorted(word))
        
        #if word after being sorted already is in dict append it in
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
            
    new_list = list(anagrams.values())
    print(anagrams)
    print("\n")
    print(new_list)

if __name__ == "__main__":
    main()