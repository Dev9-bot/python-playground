with open(r"D:\Coding\Python\FreshmanMonarch\File Handling\player.txt", "r") as file:
    player = {}

    for line in file:
        key, value = line.split(":")
        key = key.strip()
        value = value.strip()

        if key == "level" or key == "XP":
            value = int(value)

        player[key] = value

print(player)

print(player["name"])
print(player["weapon"])
print(player["XP"]+50)