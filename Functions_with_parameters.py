#def hello_func(greeting, name):
    #return '{}, {}!'.format(greeting, name)
#print(hello_func('Yo', 'Shawty'))
def player_stats(name, lvl, xp):
    return 'Player: {}\nLevel: {}\nXP: {}'.format(name, lvl, xp)
print(player_stats('Dev','5','750'))
def add_stats(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
add_stats(strength=10, agility=8, intelligence=7)