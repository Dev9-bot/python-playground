owned = {"Vandal", "Phantom", "Sheriff"}
shop = {"Vandal", "Operator", "Odin", "Ghost"}
print("Already owned and in shop:", owned & shop)
print("Available to buy:", shop - owned)
print("All weapons:", owned | shop)
weapon = input("Enter a weapon to check: ")
if weapon in shop:
    print(weapon, "is available in the shop.")
else:
    print(weapon, "is not available in the shop.")    