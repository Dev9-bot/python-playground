class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d= Dog("Coco", 4)
d.set_age(6)
print(d.get_age())  # Output: 6




#d2= Dog("Stella", 2)
#print(d2.get_age())  # Output: 2    
#d= Dog()  
#print(d.add_one(5))  # Output: 6
#print(type(d))  # Output: <class '__main__.Dog'> 