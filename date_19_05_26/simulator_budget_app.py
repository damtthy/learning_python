class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        
        items = ""
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
            
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):

    spent_per_category = []
    for cat in categories:
        spent = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spent_per_category.append(spent)
        
    total_spent = sum(spent_per_category)
    
    percentages = []
    for spent in spent_per_category:
        if total_spent == 0:
            percentages.append(0)
        else:
            percentages.append(int((spent / total_spent) * 10) * 10)


    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"


    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"


    max_len = max(len(cat.name) for cat in categories)
    names_lines = []
    
    for i in range(max_len):
        line = "     "
        for cat in categories:
            if i < len(cat.name):
                line += cat.name[i] + "  "
            else:
                line += "   "
        names_lines.append(line)
        
    chart += "\n".join(names_lines)
    return chart
