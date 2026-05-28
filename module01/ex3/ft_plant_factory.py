#!/usr/bin/env python3
class Plant:
    def __init__(self, name, starting_height, starting_age):
        self.name = name
        self.height = starting_height
        self.age = starting_age
        self.show("Created: ")

    def show(self, title=""):
        print(f"{title}{self.name}: {self.height:.1f}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    Plant("Rose", 25, 30)
    Plant("Oak", 200, 365)
    Plant("Cactus", 5, 90)
    Plant("Sunflower", 80, 45)
    Plant("Fern", 15, 120)
