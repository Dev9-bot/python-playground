
name = input("Enter your name: ")
lvl = int(input("Enter your level: "))
xp = int(input("Enter your XP: "))

print(
    f"{name}, you have {lvl} points to allocate "
    f"and {xp} XP available."
)

total_points = 0

while total_points != lvl:
    strength = int(input("Points for strength: "))
    speed = int(input("Points for speed: "))
    intelligence = int(input("Points for intelligence: "))

    total_points = strength + speed + intelligence

    if total_points != lvl:
        print("Incorrect allocation. Try again.")
    else:
        print("Points allocated correctly.")

player = {
    "name": name,
    "level": lvl,
    "xp": xp,
    "strength": strength,
    "speed": speed,
    "intelligence": intelligence
}

with open(
    r"D:\Coding\Python\FreshmanMonarch\File Handling\player.txt",
    "w"
) as file:
    for key, value in player.items():
        file.write(f"{key}: {value}\n")

print("Stats saved successfully.")

read_stats = input("Do you want to read the stats? (y/n): ")

if read_stats.lower() == "y":
    with open(
        r"D:\Coding\Python\FreshmanMonarch\File Handling\player.txt",
        "r"
    ) as file:
        print(file.read())