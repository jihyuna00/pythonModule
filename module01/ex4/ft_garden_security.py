#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = height if height >= 0 else 0
        self._age = age if age >= 0 else 0
        self.show("Plant created: ")

    def show(self, title=""):
        print(
            f"{title}{self._name}: {self._height:.1f}cm, {self._age} days old"
        )

    def update_attribute(self, attr_name, value):
        if attr_name == "height":
            attr_title = "Height"
        else:
            attr_title = "Age"
        if value < 0:
            print(f"{self._name}: Error, {attr_name} can't be negative")
            print(f"{attr_title} update rejected")
        else:
            if attr_name == "height":
                self._height = value
                unit = "cm"
            else:
                self._age = value
                unit = " days"
            print(f"{attr_title} updated: {value}{unit}")

    def set_height(self, value):
        self.update_attribute("height", value)

    def set_age(self, value):
        self.update_attribute("age", value)

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-1)
    rose.set_age(-1)
    print()
    rose.show("Current state: ")
