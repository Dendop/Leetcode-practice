import re

def main():
    
    email_list = []

    try:
        with open("email_exchanges.txt", "r") as file:
            pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        
        
<<<<<<< Updated upstream
            for line in file:
                emails = re.findall(pattern, line)
                email_list.extend(emails)
                
        print(email_list)
    
    except FileNotFoundError:
        print("File has not been found")
        
=======
        for line in file:
            emails = re.findall(pattern, line)
            email_list.extend(emails)
              
    print(email_list)
    how_many = len(email_list)
    print(how_many)
>>>>>>> Stashed changes
                
            
    
    
    
if __name__ == "__main__":
    main()