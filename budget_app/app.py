class Category:
    def __init__(self,cat_name):
        self.total = 0.0
        self.cat_name = cat_name
        self.ledger = []
        
    #categories do not share deposit
    def deposit(self,ammount,description = ""):
        self.ammount = ammount
        self.total += ammount
        self.description = description
        self.ledger.append({"ammount": float(f"{ammount:.2f}"), "description":description})
        
    
    def withdraw(self, ammount, description = ""):
        self.ammount = ammount
        if ammount > self.total:
            return False   
        self.total -= ammount
        self.description = description
        self.ledger.append({"ammount": -ammount, "description": description})
        return True
    
    def get_balance(self):
        print(f"Current Balance of {self.cat_name} : {self.total:.2f}")
        
    def transfer(self, ammount, add_to):
        self.ammount = ammount
    
    def __str__(self):
        #Title 30 characters * each, title centered in middle
        #rest 23 chars for description, 7 chars for int decimal(7,2)
        #some_string = ""
        #for i in self.ledger:
        return f"{self.cat_name}\n{self.ledger}\n{self.total:.2f}"
    
def create_spend_chart(categories):
    pass

def main():
    food = Category("Food")
    food.deposit(500, 'deposit')
    food.withdraw(100, "babanas")
    clothing = Category("Clothing")
    clothing.deposit(400, 'deposit')
    clothing.withdraw(350, 'new t-shirt')
    print(food)
    print(clothing)
    






if __name__ == "__main__":
    main()