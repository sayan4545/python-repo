# Class -02
#Operators in python
#1. Arithmatic operators
# print(5+1)
# a = 8
# b = 4
# print(a+b)#12
# print(a-b)#4
# print(a*b)#32
# print(a/b)#2
# print(a%b)#0
# print(a//b)#2 shows the integer equivalent of normal division
# print(5**2) # 25 power of operator. 5^2
# 2. relational operator

# print(4>2)
# print(5<17)
# print(4==4)
# print(4!=4)
# print(5>=5)

# 3. Logical operators

# print(1 and 0)
# print(1 or 0)
# print(not 1)
# print(not 0)

# 4. Bitwise operators
# print(2 & 3) # bitwise and operator
# print(1 & 4)
# print(2 | 3)  # bitwise or operator
# print(2 ^ 3) # bitwise XOR operator -- if both are same , answer is 0, else 1
# print(~3) # bitwise not operator
# print(3>>2) # right shift operator
# print(3<<2) # left shift operastor
# 5. Assignment operator

# c = 10
# c += 2
# print(c)
# 6 . Membership operator
# in/not in
# print('H' in 'Hello')
# print('c' not in 'cat')
# program to find the sum of of the digits in a 3 digit number
# num = int(input("Enter the number: "))
# sum = 0
# while(num!=0):
#     rem = num%10
#     sum = sum+rem
#     num = num//10
# print(sum)

# emailId = 'sayan@gmail.com'
# password = 'sayan1234'

# enterredEmail = input("Enter the email id: ")
# enterredPassword = input("Enter the password: ")

# # if(enterredEmail == emailId and enterredPassword == password):
# #     print("accepted")
# # else:
# #     print("Not accepted!")

# if(enterredEmail == emailId and enterredPassword == password):
#     print("Welcome")
# elif(enterredEmail == emailId and enterredPassword!= password):
#     print("Incorrect password, try once more")
#     enterredPassword = input("Enter the password again: ")
#     if(enterredPassword == password):
#         print("Welcome!")
#     else:
#         print("Password mismatched again, try later")
    
# else:
#     print("emailid is incorrect, reset")


# Find minimum of three numbers
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# if(num1 == num2 and num2 == num3):
#     print("The largest number is : ",num1)
# elif(num1 > num2 and num1 > num3):
#     print("The biggest number is : ",num1)
# elif(num2 > num3):
#     print("The biggest number is : ",num2)
# else:
#     print("The biggest number is : ",num3)

#Modules in python
# import math
# print(math.factorial(5))

# print(math.floor(6.8))
# print(math.ceil(6.8))

# import keyword
# print(keyword.kwlist)

# import random
# print(random.randint(1,100))

# import datetime
# print(datetime.datetime.now())

# #loops

# num = int(input("Enter the number: "))
# i = 10
# while(i!=0):
#     print(num ," * ", i  ," : ", "= ",num*i)
#     i = i-1

# # while with else
# x = 1
# while(x<3):
#     print(x)
#     x+=1
# else:
#     print("End")

# guessing game code
# import random
# jackpot = random.randint(1,5)
# inputNumber = int(input("Enter the number : "))


# while(inputNumber!=jackpot):
#     if(inputNumber>jackpot):
#         print("Guess lower")
        
#     else:
#         print("Guess higher")
#     inputNumber = int(input("Enter the number: "))
# else:
#     print("You won!!")

# import random

# jackpot = random.randint(1, 5)
# attempts = 0  # Initialize a counter for attempts
# inputNumber = int(input("Enter the number: "))

# while inputNumber != jackpot:
#     attempts += 1  # Increment the counter for each attempt
#     if inputNumber > jackpot:
#         print("Guess lower")
#     else:
#         print("Guess higher")
#     inputNumber = int(input("Enter the number: "))
# else:
#     attempts += 1  # Increment the counter for the final correct guess
#     print("You won!!")
#     print(f"It took you {attempts} attempts to guess the correct number.")


# for i in range(1,10,2):
#     print(i)

# for i in 'Chittaranjan':
#     print (i)


population = 10000
rateOfGrowth = 0.10

for i in range (1,10):
    population = population * rateOfGrowth + population
    print("population at the end of year ",i,": ",population)

# Calcul;ate the sequenxce till the nth term
#1/1! + 2/2! +...

n = int(input("Enter the nth term: "))
import math
sum = 0
for i in range(1,n+1):
    sum = sum + i/math.factorial(i)
print(sum)








