#Find the length of a string without using the len() function

# a = input('Enter the string: ')
# count = 0
# for i in a:
#     count = count+1
# print('The length of the string is : ',count)

# Extract the username from a given string.
# eg: sayanchatterjee3010@gmail.com, you have to extract sayanchatterjee

# gmail = input("Enter the email : ")
# username_list = gmail.split("@")
# print(username_list)
# username = username_list[0]
# print(username)

# Calculate the frequency of a particular character in a string
# str = '''
# Hello , How are you.
# '''
# count = 0
# for i in str.casefold() :
#     if i is 'h':
#         count = count + 1
# print(count)
# print('The frequency of h is : ',count)
# print('The frequency of h is : ',str.casefold().count('h'))

# A program to remove a particular character from a string

str = input("Enter the string: ")
character = input("Enter the character: ")
for i in str:
    if i is character:
        continue
    print(i,end ="")
print()

