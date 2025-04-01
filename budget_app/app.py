class Category:
    def __init__(self,cat_name):
        self.total = 0.0
        self.cat_name = cat_name
        self.ledger = []
        
    #categories do not share deposit
    def deposit(self,amount,description = ""):
        self.total += amount
        self.ledger.append({"amount": float(f"{amount:.2f}"), "description":description})
        
    
    def withdraw(self, amount, description = ""):
        if amount > self.total:
            return False   
        self.total -= amount
        self.ledger.append({"amount": -amount, "description": description})
        return True
    
    def get_balance(self):
        print(f"Current Balance of {self.cat_name} : {self.total:.2f}")
        
    def transfer(self, amount, category):
        if amount > self.total:
            return False
        self.total -= amount
        self.ledger.append({"amount": -amount, "Transfer to": category.cat_name})
        category.ledger.append({"amount": amount, "Transfered from:": self.cat_name})
        category.total += amount
        return True
    
    def check_funds(self, amount):
        
        if amount > self.total:
            return False
        return True
    
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
    food.deposit(900,'deposit')
    food.withdraw(45.67, 'milk,cereak,eggs,bacon,bread')
    clothing = Category("Clothing")
    clothing.deposit(400, 'deposit')
    clothing.withdraw(350, 'new t-shirt')
    food.transfer(300,clothing)
    print(food)
    
    




if __name__ == "__main__":
    main()