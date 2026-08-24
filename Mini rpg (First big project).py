Menu = ["1.View Player", "2.View Inventory", "3.Add Item", "4.Remove Item", "5.Level Up", "6.Attack", "7.Quit"]
Player = {
    "name": "Dev",
    "Level": 1,
    "health": 100,
    "weapon": "Sword",
    "rank": "Bronze"
}
inventory = ["Sword", "Potion", "Shield"]

while True:
    print("Welcome to the Mini RPG Game!")
    print("Menu:")
    for option in Menu:
        print(option)
    choose = input("Choose an option: ")

    if choose == "1":
        for key, value in Player.items():
            print(key, ":", value)
    elif choose == "2":
        for i, weapon in enumerate(inventory):
            print(i + 1, weapon)
    elif choose == "3":
        item = input("Enter the item you wanna add: ")
        inventory.append(item)
        print("Item added to inventory")
    elif choose == "4":
        item = input("Enter item you wanna remove: ")
        if item in inventory:
            inventory.remove(item)
            print("Item removed from inventory")
        else:
            print("Item not found in ya inventory")
    elif choose == "5":
        Player["Level"] += 1
        print("You LEVELED UP! You are now level", Player["Level"])
    elif choose == "6":
        import random

        def attack():
            attack = random.randint(10, 30)
            return attack

        print("You attacked the enemy and dealt", attack(), "damage!")
    elif choose == "7":
        print("Thanks for playing!")
        break