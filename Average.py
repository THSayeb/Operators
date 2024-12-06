print("Hello \n Here you can find the average height of your 5 trees")
print("Now, provide the lenths inches")

t1 = float(input("provide the height"))
t2 = float(input("Provide next height"))
t3 = float(input("Provide next height"))
t4 = float(input("Provide next height"))
t5 = float(input("Provide next height"))

#Addition
sum = t1 + t2 + t3 + t4 + t5
print("The sum of the heights is ", sum, " inches")

#Average
aver = sum/5
print("The averge height is ", aver, " inches")
