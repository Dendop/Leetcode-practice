def square_sum(numbers):
    #your code here
    results = []
    t = 0
    for i in numbers:
        t = i ** 2
        results.append(t)
    return sum(results)



def main():
    a_list = [3,4,0,9]
    magic = square_sum(a_list)
    print(magic)




if __name__ == "__main__":
    main()