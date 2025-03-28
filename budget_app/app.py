class Category:
    def __init__(self,cat_name):
        self.total = 0.0
        self.cat_name = cat_name
        self.ledger = []
    
    def deposit(self,ammount,description = ""):
        self.ammount = ammount
        self.total += ammount
        self.description = description
        self.ledger.append({"ammount":ammount, "description":description})
    
    def withdraw(self, ammount, description):
        self.ammount = ammount
        self.total -= ammount
        if self.total < 0:
            return False
        self.ledger.append({"ammount": ammount, "description": description})
        
    def __str__(self):
        return f"*************{self.cat_name}************\n{self.ledger}\n{self.total}"
def create_spend_chart(categories):
    pass

def main():
    food = Category("Food")
    food.deposit(500, 'deposit')
    food.withdraw(100, "babanas")
    print(food)







if __name__ == "__main__":
    main()