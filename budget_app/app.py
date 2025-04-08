class Category:
    def __init__(self,cat_name):
        self.total = 0.0
        self.cat_name = cat_name
        self.ledger = []
        
    #categories do not share deposit
    def deposit(self,amount,description = ""):
        self.total += amount
        self.ledger.append({"amount": amount, "description":description})
        
    
    def withdraw(self, amount, description = ""):
        if amount > self.total:
            return False   
        self.total -= amount
        self.ledger.append({"amount": -amount, "description": description})
        return True
    
    def get_balance(self):
        return self.total
        
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.cat_name}") #if amount < total then -amount
            category.deposit(amount, f"Transfer from {self.cat_name}")
            return True
        return False

        
        
    def check_funds(self, amount):
        if amount > self.total:
            return False
        return True
    
    def __str__(self):
        title = f"{self.cat_name:*^30}\n" #centered to middle, 30 characters filled with *
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]
            amnt = f"{entry['amount']:>7.2f}"
            items += f"{desc:23}{amnt}\n"
        total_line = f"Total: {self.total:.2f}"
        return title + items + total_line
    
def create_spend_chart(categories):
    title = "Percentage spent by category"

def main():
    food = Category("Food")
    food.deposit(900,'deposit')
    food.withdraw(45.67, 'milk,cereak,eggs,bacon,bread')
    clothing = Category("Clothing")
    clothing.deposit(400, 'deposit')
    clothing.withdraw(350, 'new t-shirt')
    food.transfer(50,clothing)
    print(food)
    
    




if __name__ == "__main__":
    main()