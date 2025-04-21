class Cat:
    

    def __init__(self, name, breed):

        self.name = name
        self.breed = breed
        print(f"A new cat named {self.name} ({self.breed}) has been created!")

    def meow(self):
        
        print("Meow!Meow!")

    def raise_tail(self):
        
        print(f"{self.name} raises its tail happily!")


my_cat = Cat("Joleen", "Calico")
another_cat= Cat("Masha", "Tabby cat")

print("\n--- Cat Actions ---")
my_cat.meow()
my_cat.raise_tail()

print("\n--- Another Cat's Action ---")
another_cat.meow()