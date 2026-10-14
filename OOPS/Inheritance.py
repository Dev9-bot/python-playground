class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I don't know what I say.")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color              

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old and my color is {self.color}.")    

class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print("Woof")

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old and my breed is {self.breed}.")    

d1 = Dog("Stella", 2, "German Shepherd")
d1.speak()
d1.show() 
c1 = Cat("Baagheera", 4, "Black")
c1.speak()
c1.show()
