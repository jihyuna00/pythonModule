#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, days, growth_rate=1):
        self.name = name
        self.height = height
        self.days = days
        self.growth_rate = growth_rate

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")

    def grow(self):
        self.height += self.growth_rate

    def age(self):
        self.days += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")

    rose = Plant("Rose", 25.0, 30, 0.8)
    rose.show()

    initial_height = rose.height

    for day in range(1, 8):
        rose.grow()
        rose.age()

        print(f"=== Day {day} ===")
        rose.show()

    print(f"Growth this week: {round(rose.height - initial_height, 1)}cm")
