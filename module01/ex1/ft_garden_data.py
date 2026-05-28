#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
#    my_rose = Plant("Rose", 25, 30)
#    my_sun = Plant("Sunflower", 80, 45)
#    my_cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.show()
#    my_rose.show()
#    my_sun.show()
#    my_cactus.show()
