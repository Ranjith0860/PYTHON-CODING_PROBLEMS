# #decorators

# def sub(r):
#   def inner(*args, **kwargs):
#     if len(args) != 2:
#         print("Expected exactly two arguments")
#         return
#     a, b = args
#     if a % 2 == 0 and b % 2 == 0:
#         r(a, b)
#     else:
#         print("hii")



# @ sub
# def subb(a,b):
#     print(a-b)
# subb(10,7)






def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function called with: args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Ranjith")
greet("Ranjith", greeting="Hi")
