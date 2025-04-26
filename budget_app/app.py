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
    #calculate spent for each category
    spent_category = []
    for cat in categories:
        spent = 0
        for entry in cat.ledger:
            if entry['amount'] < 0: #this checks if it's - value
                spent += -entry['amount']
        spent_category.append(spent) #add the value into list
    total_spent = sum(spent_category) #sums all values in list
    
    #calculate percentage
    percentage = []
    perc = 0
    for each in spent_category:
        perc = int((each / total_spent) * 100) // 10 * 10 #if 33% 33 // 10 = 3 * 10 = 30, rounding
        percentage.append(perc)
    
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10): #start, stop, steps
        line = f"{i:>3}|" #3 characters aligned to right
        for percent in percentage:
            line += " o " if percent >= i else "   " #if percent is equal or higher then o else empty string
        line += " "
        chart += line + "\n"

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    max_len = max(len(c.cat_name) for c in categories)
    for i in range(max_len):
        line = "    "
        for cat in categories:
            letter = cat.cat_name[i] if i < len(cat.cat_name) else " "
            line += f" {letter} "
        line += " "
        chart += line + "\n"

    return chart.rstrip("\n")
    

def main():
    food = Category("Food")
    food.deposit(900,'deposit')
    food.withdraw(45.67, 'milk,cereak,eggs,bacon,bread')
    clothing = Category("Clothing")
    clothing.deposit(400, 'deposit')
    clothing.withdraw(350, 'new t-shirt')
    food.transfer(50,clothing)
    #print(food)
    print(create_spend_chart([food,clothing]))
    
    




if __name__ == "__main__":
    main()