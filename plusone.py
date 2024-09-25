def main():
    
    digits = [4, 3, 2, 1]
    
    result = ""
    plusone = 0
    
    for num in digits:
        
        
        result += str(num)
    plusone = int(result) + 1
    digits.clear()
    for item in str(plusone):
        digits.append(int(item))
       
    
    print(digits)
    
    

if __name__ == "__main__":
    main()