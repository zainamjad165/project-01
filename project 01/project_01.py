# Age Calculator
birth_year = int(input('what year were you born?  '))
age = 2022 - birth_year
print(f'your age is: {age}')
print('\n\n')

#Password Length Checker
username = input('Enter your username:  ')
password = input('Enter your password:  ')
length = len(password)
hidden_password = '*' * length
print(f'{username} your password, {hidden_password} , is {length} letters long.')
print('\n\n')

# Password Checker
password=int(input('what is your password:  '))
if password == 1234 :
    print('hello')
else:
    print('wrong password')
print('\n\n')

#Logical Operators
is_magician = True
is_expert = False
#chek if magician AND expert: "you are a master magician"
if is_magician and is_expert:
    print('you are a master magician.')
#chek if magician but not expert: "at least you are getting there"
elif is_magician and not is_expert:
    print('at least you are getting there.')
#chek if not a magician: "you need magical powers"
else:
    print('you need magical powers.')
print('\n\n')

# Counter
my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0
for item in my_list:
    counter = counter + 1
print(counter)
print('\n\n')

# Find Duplicates in list
some_list = ['a','b','c','b','d','m','n','n']
duplicates = []
for item in some_list:
    if some_list.count(item)>1:
        if item not in duplicates:
            duplicates.append(item)
print(duplicates)
print('\n\n')

# TESLA
#1.
def checkDriverAge():
    Age = input("What is your age?: ")
    if int(Age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(Age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(Age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

#2.
def checkDriverAge(Age=0):
    if int(Age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(Age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(Age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
print('\n\n')

# Find the highest even
def highest_even(li):
    evens = []
    for item in li:
        if item % 2 ==0:
            evens.append(item)
    return max(evens)
print(highest_even([10,2,3,4,8,11]))

