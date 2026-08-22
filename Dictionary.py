player = {
    "name": "Dev",
    "Level": 18,
    "weapon": "Vandal"
}
print(player["weapon"])
player["weapon"] = "Operator"
print(player["weapon"])
player["rank"] = "Gold"
print(player["rank"])
player.pop("Level")
print(player.get("skin", "No skin equipped"))
for key, value in player.items():
    print(key,":", value)