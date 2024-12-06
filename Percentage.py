print("Here, you can find the percentage of you marks \n First,")

total = float(input("Enter total number of whole exam "))
bnum = float(input("Enter Bangla number "))
enum = float(input("Enter English number "))
mnum = float(input("Enter Math number "))

print("___________________________________________________________")

sum = bnum + enum + mnum
print("Your total number is ", sum)

per = (sum/total)*100
print("Percentage = ", per)