name = input("Enter your name: ")
lvl = input("Enter your Lvl: ")
xp = input("Enter your XP: ")
print(name, "You have", lvl, "points to put into str speed and int. You have", xp, "XP to spend on upgrading.")
strength = int(input("How many points do you want to put into strength? "))
speed = int(input("How many points do you want to put into speed? "))  
intelligence = int(input("How many points do you want to put into intelligence? "))
total_points = strength + speed + intelligence
if total_points <= int(lvl):
    print("Points allocated correctly.")
else:
    print("Error: The total points allocated do not match your level.")
player = {
    "name": name,
    "level": int(lvl),
    "xp": int(xp),
    "strength": strength,
    "speed": speed,
    "intelligence": intelligence
}
with open(r"D:\Coding\Python\FreshmanMonarch\File Handling\player.txt", "w") as file:
    for key, value in player.items():
       file.write(f"{key}: {value}\n")
read_file = input("Do you want to read the stats? (yes/no): ")

if read_file.lower() == "yes":
    with open(r"D:\Coding\Python\FreshmanMonarch\File Handling\player.txt", "r") as read_file:
        print(read_file.read())
else:
    print("Stats saved successfully.")    