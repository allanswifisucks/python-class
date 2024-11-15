# Amit Modi
# 6:37 PM
# Ask user a few questions: (example questions)

# What type of expense:
# What is the amount:
# Description:
# Date of expense:
# `Add atleast 5 questions.

# Store it in a list: (using append())

# [ food, 10, I ate a burger, fun, 20, slides ] -- BAADD

# ------------------------------------------------------

# Make it like this:

# [

#  {expense: food,

# amount: 10,

#   description: I ate a burger} ,

#   {expense: fun,

#   amount: 20,

#   description: slides}

# ]

# Hint: U can google this:

# Create a List of dictionaries.
# variable_name = {"description": description, "amount": amount, "category": category}
expencelist=[]



def addexpence():



    while True:

        expence=input("whats the expence\n")
        cost=input("whats the cost\n")
        description=input("whats the description\n")
        date=input("whats the whats the date\n")
        location=input("whats the location\n")
#this asks for the expence and stuff 

        expencedict= {"expence":expence,"cost":cost,"description":description,"date":date,"location":location}

        expencelist.append(expencedict)

        print("your expence has been added\n")
        print(expence,cost,description,date,location)
        con=input("do you want to continue\n")
        if con==("yes"):
            print("ok")
        if con==("no"):
            break
#this asks if you want to continue
def vebc():
    print("the catergorys are\n")
    for g in expencelist:
    
        print(g["expence"])
    
    categorychoice=input("chose a category")
    for h in expencelist:
        if categorychoice==h["expence"]:
            print(h)
        con1=input("do you want to continue\n")
        if con1==("yes"):
            print("ok")
        if con1==("no"):
            break
def calculatetotalexpenses():
    costtotal=0

    for f in expencelist:
        costtotal+=f["cost"]
    print(f"the total is\n{costtotal}")   
    

def viewexpenses():
    for I in expencelist:
        print(I)
#This makes a for loop       

while True:
    print("1.add expence\n2.veiw expences\n3.calculate total expenses\n4.view expenses by catergory\n5.save expence\n6.Qwit")
# This shows the menu 
    menu=input("Choose an option\n")
    if menu=="1":
        addexpence()
    if menu=="2":
        viewexpenses()
    if menu=="3":
        calculatetotalexpenses()
    if menu=="4":
        vebc()    
    if menu=="5":
        continue    
    if menu=="6":
        break
#you chose a menu opption 

# 3. Calculate Total Expenses
# 4. View Expenses by Category
# 5. Save Expenses