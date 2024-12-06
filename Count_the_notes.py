print("Welcome to this app \n Here, you will be able to calculate how many notes do you need to fulfil the payment")
print("Frist, Enter the amount")

am = float(input("Enter the amount  "))
n100 = am//100
n50 = (am %100)//50
n10 = ((am % 100)%50)//10

print("100 notes ", n100 )
print("50 notes ", n50)
print("10 notes ", n10)