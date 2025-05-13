def is_square(n:int):
    if n < 0:
        return False
    root = int(n ** 0.5)
    if root * root == n:
        return True
    else:
        return False
        
    
def main():
    magic = is_square(26)
    print(magic)
    
if __name__ == "__main__":
    main()