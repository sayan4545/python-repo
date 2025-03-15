# #strings
# name = "Daniel"
# print(name)
# name2 = "Daniel"
# print(name==name2)
# print(id(name),id(name2))

# a = 56
# b = 56
# print(id(a),id(b))
# a = 64
# print(id(a),id(b))
# In python strings are sequence of unicode characters.
# s = "It's raining outside.."
# print(s)

# p = ''' hey this is is an example 
# of multiline string in python..
# '''
# print(p)

# str = "Sayan Chatterjee"
# print(str[1])
# print(str[1:4])
# print(str[:7])
# print(str[3:])
# print(str.upper())
# print(str.replace("a","z"))
# print(id(str),id(str.upper()),id(str.lower()))

# print(str[-1:])
# print(str[::-1].upper())

# a = "world"
# print(a[-1:-6:-1])

# python strings are immutable.

# a = "Sayan"
# a = "Chandrika"
# print(a)
# The above example is not immutable behaviour of python strings

# a[2] = "D"
# print(a)
# The above example shows the immutable behaviour.

# deleteing a string

# del a

# s = "hello World"
# del s[-1:-5:2]
# print(s) -- String doesnot allow item deletion


# Arithmatic operators --> +,* --> can concatenate only string to string.
# a = "Hello "
# print(a+"world")
# print(a*2)

# Relational operator 

# print("Delhi" == "Mumbai")
# print("sayan" > "Chandrika") # Checks the lexicographical order that is calculated based on the unicode values.
# print("Harshit" == "harshit")

# print("Mega Mart" > "Movie Maniac")
# print("Sayan" > "Sayan".lower())

# print("hello" and "world")
# print('hello' or 'world')
# print(not 0)

# a = "Kane Williamson"
# for i in a :
#     if i == " ":
#         continue
#     print(i, end=",")
# print()

# i = 0
# while(i!=len(a)):
#     print(a[i:i+1],end =",")
#     i = i+1
# for i in "Delhi":
#     print("Sayan",end =" ")
# print()
# print('D' in 'Delhi')
# print('s' in 'Sayan'.casefold()) # To ignore lower and upper case.

# print(max("Sayan")) # Returns the one with the highest unicode value.
# print(min("Chandrika"))

# print(sorted("chandrika")) #Return a new list containing all items from the iterable in ascending order.

# userName = 'sayanchatterjee3010@gmail.com'
# print(userName.capitalize()) # makes the first element capuital

# name = 'sayan chatterjee'
# print(name.title())
# print(id(name),id(name.title())) # Both have different memory address


# name2 = 'chandrika'
# print(name2.find('d'))
# print(name2.count('k'))
# print(name2.index('r'))

# print(name2.startswith('c'))# true
# print(name2.endswith('h'))# false

# firstName = input("Enter the first name: ")
# lastname = input("Enter the last name : ")
# print('Name recorded was {} {}'.format(firstName,lastname))

# userName = input("Enter the username: ")
# password = input("Enter the password: ")
# print(userName.isalnum())
# print(userName.isalpha())
# print(password.isalpha())
# print(password.isalnum())

str = '''
Hello, My name is Sayan Chatterjee, Currently in a bootcamp.
'''
print(str.split(','))
print(str.split())