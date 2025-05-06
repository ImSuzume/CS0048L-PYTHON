
'''
#syntax

def function_name(parameters):
    """ doc string """
    #function body
    return 
'''
# def greet(name):
#     """Function greets the person and name as the parameter"""
#     print ("Hello "+name+". Good morning ")

# greet("Hadji")

# def display_hello():
#     """
#         documentation
#         this display the hello message
    
#     """
#     print ("This display the hello message")

# #display_hello()
# print (display_hello.__doc__)

#Function Arguments
#positional Arguments

# def greet (name, message):
#     print (message,name)

# greet("Hadji","Hello")

#default Arguments

# def greet(name,message="Hi"):
#     print (message,name)

# greet("Hadji")
# greet("James","Hi there...")

#arbitrary arguments (number of arguments (*args))

# def greet(*names):
#     for name in names:
#         print ("Hello", name)

# greet("Aida","Lorna","Fe")

#return statement

# def add(a,b):
#     return a+b
    
# result = add(3,5)
# print (result)
# print (add(10,5))


# #scope of variables
# #local variables - var is inside a function- access it within the function 
# #global variable - var define outside of a function, accessible anywhere

# x = 10  #global var 
# def abc():
#     y = 15
#     print ("Values of variables ", x,y)

# abc()
# print ("Outide of the function code ")

# #modify the global variable 
# counter = 0 

# def increase_counter():
#     global counter
    
#     counter += 1 
#     print (f"Inside the function, counter = {counter}")

# print (f"Before calling the function, counter = {counter}")
# increase_counter()
# print (f"After calling the function, counter = {counter}")

    
# #global varible access to multiple functions 
# global var 
# balance = 1000

# def deposit(amount):
#     global balance 
#     balance += amount 
#     print (f"After deposit, New balance is {balance}")

# def withdraw(amount):
#     global balance
#     if amount <= balance:
#         balance -= amount 
#         print (f"After withdraw, New balance is {balance}")
#     else:
#         print ("Inssuficient balance ")

# print (f"Initial Balance is {balance}")
# deposit(500)
# withdraw(200)
# withdraw(2000)
# print (f"current Balance is {balance}")



# #lambda functions
# double = lambda x: x*2

# print(double(5))

# def double(x):
#     return x * 2

# print(double(5))

# add = lambda x, y: x+y
# print(add(5,10))