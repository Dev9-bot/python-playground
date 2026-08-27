with open(r"D:\Coding\Python\FreshmanMonarch\File Handling\player.txt", "w") as file:
    file.write("Name: Dev\n")
    file.write("Level: 2\n")
    file.write("Weapon: Vandal\n")
    file.write("Rank: Gold\n")
    file.write("XP: 150\n")
with open(r"D:\Coding\Python\FreshmanMonarch\File Handling\player.txt", "r") as file:
    print(file.read())