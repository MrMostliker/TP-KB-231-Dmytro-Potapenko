class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Alice", 30)
print(person1.name) #Outcome "Alice"

print(person1) #Outcome "<__main__.Person object at 0x000002AE9123E060>"

class Unit:
    def __init__(self, cost, damage):
         self.cost = cost
         self.damage = damage
         
    def __str__(self):
        return f"Unit (Ціна={self.cost}, шкода={self.damage})"
    
warrior = Unit(100, 5)
print(warrior)     #Outcome: "Unit (Ціна=100, шкода=5)"
        

