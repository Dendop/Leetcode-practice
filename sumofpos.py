def positive_sum(arr: list):
    total = 0
    for each in arr:
        if each > 0:
            total += each
    return total
    
def main():
    magic = positive_sum([1, -2 , 3, 4, 5])
    print(magic)

if __name__ == "__main__":
    main()