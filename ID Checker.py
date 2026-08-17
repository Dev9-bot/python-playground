age= int(input("What is your age?"))
if age > 18:
    has_id = input("Do you have an ID? (y/n): ")
    if has_id== "y":
        print("You are allowed to enter.")
    else:
        print("You are not allowed to enter without an ID.")
else:
    print("You are not allowed to enter because you are under 18.")