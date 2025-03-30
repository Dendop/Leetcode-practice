class Category:
    def __init__(self,cat_name):
        self.total = 0.0
        self.cat_name = cat_name
        self.ledger = []
        self.current_total = 0
    #categories do not share deposit
    def deposit(self,ammount,description = ""):
        self.ammount = ammount
        self.total += ammount
        self.description = description
        self.ledger.append({"ammount": float(f"{ammount:.2f}"), "description":description})
        
    
    def withdraw(self, ammount, description = ""):
        if self.total < 0:
            return False
        self.ammount = ammount
        self.total -= ammount
        self.description = description
        self.ledger.append({"ammount": -ammount, "description": description})
        
    def __str__(self):
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
    clothing.withdraw(150, 'new t-shirt')
    print(food)
    print(clothing)






if __name__ == "__main__":
    main()