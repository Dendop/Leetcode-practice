def alphabet_position(text):
    text = text.lower()
    positions = []

    for char in text:
        if 'a' <= char <= 'z':
            position = ord(char) - 96
            positions.append(str(position))

    return " ".join(positions)

def main():
    text = "The sunset sets at twelve o' clock."
    
    lets_see = alphabet_position(text)
    print(lets_see)
    print(ord('a'))

if __name__ == "__main__":
    main()