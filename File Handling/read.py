file = open(r"D:\Coding\Python\FreshmanMonarch\File Handling\player.txt", "r")
for line in file:
    print(line.strip())
file.close()