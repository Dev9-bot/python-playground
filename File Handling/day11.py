player = {
    "name": "Dev",
    "level": 2,
    "weapon": "Vandal",
    "rank": "Gold",
    "XP": 150
}
with open(r"D:\Coding\Python\FreshmanMonarch\File Handling\player.txt", "w") as file:
        for key, value in player.items():
                file.write(f"{key}: {value}\n")
                