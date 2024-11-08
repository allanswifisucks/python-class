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
        

        expencedict= {"expence":expence,"cost":cost,"description":description,"date":date,"location":location}

        expencelist.append(expencedict)

        print("your expence has been added\n")
        print(expence,cost,description,date,location)
        con=input("do you want to continue\n")
        if con==("yes"):
            print("ok")
        if con==("no"):
            break





def viewexpenses():
    for I in expencelist:
        print(I)
print("1.add expence\n2.veiw expences\n3.quit")
while True:
   
    menu=input("Choose an option\n")
    if menu==("1"):
        addexpence()
    if menu==("2"):
        viewexpenses()
    if menu==("3"):
        break
