player = {
    "name": "Dev",
    "Level": 1,
    "health": 100,
    "weapon": "Spear"
}
player["Level"] = 2
player["health"] = 75
player["rank"] = "Gold"
for key, value in player.items():
    print(key, ":", value)