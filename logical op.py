#Author:Jessica Muthoni
# A code to solve simple math problems

num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))

ch = input("enter any operation *, +,-,/" )
result = 0

if ch =='+':
    result = num1 +num2
elif ch =='*':
    result = num1 * num2
elif ch =='-':
    result = num1 - num2
elif ch=='/':
    result = num1 / num2

else:print ("Error invalid operation")
print (result)

