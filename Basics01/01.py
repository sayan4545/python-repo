# print("hey Python!!")
# # comments :
# # data types in python : 1.Number,2 String 3 Bool 4 Set 5 Tuples 6 Dictionary 8 None 9 List
# # keywords --> Interpretor uses some reserved words that they use to convert Highlevel code to machine level code
# print("taking input from user")
# a = int(input("Enter a number: "))# casting the input to integer explicitly
# b = int(input("Enter another number: ")) # casting the input to integer explicitly.
# print("The sum of a and b is : ",a+b) # wolud result in sum of the two numbers

# c = input("Enter the first number: ")
# d = input("Enter the second number: ")
# print(c+d) # would resuylt in a string by concatenating the inputs
# print(type(c),type(d)) # str and str
# print(type(int('4')))
# firstNumber = input("Enter the first number: ")
# secondNumber = input("Enter the second number: ")
# result = int(firstNumber) + int(secondNumber)
# print(result,"type of firstNumber",type(firstNumber),"type of second number: ",type(secondNumber))
# The above code will result in sum and both type as String. because, while casting,
# python creates a copy of the object in the heap memory. changes and casting are done 
# to the copied object, not the original one.

#Literals --> The value assigned to the variables are literals
a = 0b1010  # binary
print(a)
b = 0o310 # octal representation
print(b)

raw_str = "Hey\nthis is a good T-Shirt"
print(raw_str)

