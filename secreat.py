print("welcome to this repo")
print("here we show how we use check the condition of anything ")


#fruits price
apple = 200
banana = 457
mango = 457
grapes = 230

#user buget
user_budget = 800
print("user budget is:", user_budget)
print("\nchecking purchase options...\n")

#option1: apple+grapes
total_price = apple+grapes
if total_price <= user_budget:
    print("you can buy apple and grapes")
    print("total price:", total_price)
else:
    print("you can not buy these")
    print("totl price:", total_price)


#option2: banana + mango
total_price = banana + mango
if total_price <= user_budget:
    print("you can buy banana and mango")
    print("total price:", total_price)
else:
    print("you can not buy these")
    print("totl price:", total_price)

#option3: apple+banana
total_price =apple+banana
if total_price <= user_budget:
    print("you can buy  apple andbanana")
    print("total price:", total_price)
else:
    print("you can not buy these")
    print("totl price:", total_price)

print("\nprogram finished")


#in this program we used variables,addition,if-else condition,budget check logic