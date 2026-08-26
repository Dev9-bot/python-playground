players = [
    ("Dev", 100, "Vandal"),
    ("Alice", 80, "Phantom"),
    ("Bob", 60, "Operator")
]
weapons = {"Vandal", "Phantom", "Operator", "Sheriff"}
for name, health, weapon in players:
    print(name, health, weapon)
    while True:
        choose = input(f"{name}, choose your weapon: ")

        if choose in weapons:
            print(name, "Has equipped the", choose)
            break
        else:
            print("This weapon ain't available")
            