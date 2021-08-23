class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        """
        Accepts deposit amount and description, and adds it to the ledger.
        If no description is given, it defaults to an empty string.
        """

        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        """
        This method returns the current balance of the current
        budget category using the withdrawals and deposits that
        have occurred.
        """
        sumList = []
        for i in self.ledger:
            sumList.append(i["amount"])

        sumList = sum(sumList)
        return sumList

    def check_funds(self, amount):
        """
        Accepts an amount as an argument, then checks to see if
        the amount is greater than the balance of budget category.
        If so, returns False; otherwise, returns True.
        """
        
        currentBalance = self.get_balance()
        amount = amount
        
        if amount < 0:
            amount = -(amount)

        if amount > currentBalance:
            return False
        else:
            return True

    def withdraw(self, amount, description = ""):
        """
        Takes a NEGATIVE amount, and description, passes that into the ledger.
        In order to have a successful withdrawal, the amount withdrawn must not
        exceed the total amount in the ledger.
        If successful, return True. Else, returns False.
        """
        withdraw = self.check_funds(amount)

        
        if amount > 0:
            amount = -(amount)
        
                    
        if withdraw == True:
            self.ledger.append({"amount": float(amount), "description": description})
            return True
        else:
            return False
            

    def transfer(self, amount, other):
        """
        This method adds a withdraw with a description, and then
        adds a deposit to the other budget category with the same
        amount. If there are not enough funds, no exchange should
        occur. If a transfer takes place, True is returned; else, False.
        """
        transferFrom = self.name
        transferTo = other.name
        
        if amount >  0:
            amount = -(amount)
        

        curBalance = self.get_balance()
        if -(amount) > curBalance:
            return False
        else:
            self.ledger.append({"amount": amount, "description": f"Transfer to {transferTo}"})
            other.ledger.append({"amount": -(amount), "description": f"Transfer from {transferFrom}"})
            return True


    def __str__(self):
        num = 30 - len(self.name)
        printThis = ""
        ledger = self.ledger
        
        if num%2 == 0:
            topLine = "*"*(int(num/2))+self.name+"*"*(int(num/2))
            printThis += topLine
            
        else:
            num = round(num/2)
            topLine = "*"*(int(num -1 ))+"stuff"+"*"*(int(num))
            printThis += topLine


    
        for item in ledger:
            printThis += "\n"
            curDescr = item["description"]

            if len(curDescr) == 23:
                printThis += curDescr
            elif len(curDescr) < 23:
                dist = 23 - len(curDescr)
                printThis += curDescr+" "*dist
            else:
                printThis += curDescr[:23]


            curNum = float(item["amount"])
            curNum = "{:.2f}".format(curNum)
            
            if len(str(curNum)) == 7:
                printThis += str(curNum)
            elif len(str(curNum)) < 7:
                dist = 7 - len(str(curNum))
                printThis += " "*dist+str(curNum)
            else:
                curNum = str(curNum)
                printThis += curNum[:7]
                    
        total = self.get_balance()
        printThis += "\n"
        printThis += f"Total: {total}"

        return printThis
        

def create_spend_chart(category_list):
    """
    This chart shows the percentage spend in each category passed in
    to the function. The percentage spend is calculated with withdrawals.
    """
    catList = category_list
    catNames = []
    dist = (len(catList))*"   "
    line = 100
    bar_chart = ""
    getPercent = []
    totalWith = []
    sumTotal = 0
    
    for item in catList:
        temp = 0
        for entry in item.ledger:
            if entry["amount"] < 0:
                temp += entry["amount"]
                getPercent.append(temp)

    sumTotal = sum(getPercent)
    for num in getPercent:
        temp = (num/sumTotal)*100
        temp = round(temp)
        totalWith.append(temp)


    
    bar_chart = "Percentage spent by category\n"
    while line >= 0:
        if line == 100:
            bar_chart += f"{line}| "
            for item in totalWith:
                if line <= (item):
                    bar_chart += "o  "
                else:
                    bar_chart += "   "
            bar_chart += "\n"
            line -= 10
        elif line < 100 and line > 0:
            bar_chart += " "+f"{line}| "
            for item in totalWith:
                if line <= (item):
                    bar_chart += "o  "
                else:
                    bar_chart += "   "
            bar_chart += "\n"
            line -= 10
        elif line == 0:
            bar_chart += "  "+f"{line}| "
            for item in totalWith:
                bar_chart += "o  "   
            bar_chart += "\n"
            line -= 10

    bar_chart += "    -"+"-"*(len(dist))+'\n'

    ###
    for item in catList:
        temp = item.name
        catNames.append(temp)
    ###
    maxLength = 0
    for item in catNames:
        if len(item) > maxLength:
            maxLength = len(item)


    ####
    newCatNames = []
    tempLength = 0
    tempName = ""
    for item in catNames:
        tempLength = maxLength - len(item)
        tempName = item+" "*(tempLength)
        newCatNames.append(tempName)

    ###
    for num in range(maxLength):
        bar_chart += "     "
        for item in newCatNames:
            bar_chart += item[num]+"  "
        if num != (maxLength-1):
            bar_chart += "\n"

    return bar_chart



food = Category("Food")
business = Category("Business")
entertainment = Category("Entertainment")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)


print(create_spend_chart([business, food, entertainment]))
print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")































        
