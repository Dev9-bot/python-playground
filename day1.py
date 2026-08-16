name= input("What is your name? ")
birthyear = int(input("What year were you born? "))
age =2026 - birthyear
print("Hello", name, "you are approximately" , age, "years old.")
if birthyear >= 2026:
    print("You are not born yet!")