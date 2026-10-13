#Add, subtract, multiply, and divide two numbers.
x=int(input("enter first number: "))
y=int(input("enter second number: "))
def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def divide(x,y):
    return x/y
def multiply(x,y):
    return x*y

print("Select Operations: ")
print("1.add")
print("2.substract")
print("3.divide")           
print("4.multiply")
choice=input("enter choice(1/2/3/4): ")

if choice == '1':
    print(x, "+", y, "=", add(x, y))
elif choice == '2':
    print(x, "-", y, "=", substract(x, y))
elif choice == '3':
    print(x, "/", y, "=", divide(x, y))
elif choice == '4':
    print(x, "*", y, "=", multiply(x, y))
else:
    print("Invalid input")
    
