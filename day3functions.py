def greet():
    print("Hello, Dev")
def greet_user(name):
    print("Hello,", name)
def introduce(name, age):
    print("Hello my name is", name, "and I am", age, "years old.")    
def add_numbers(num1, num2):
    return num1 + num2   
def multiply_numbers(num1, num2):
    return num1 * num2
def is_adult(age):
    if age>= 18:
        return True
    else:
        return False
#Testing
result = is_adult(20)
print(result)