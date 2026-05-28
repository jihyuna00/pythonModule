#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age

    def show(self):
        print(f"{self._name}: {self._height:.1f}cm {self._age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self._color = color
        self._is_bloom = False

    def bloom(self):
        if not self._is_bloom:
            print(f"[asking the {self._name} to bloom]")

    def show(self):
        super().show()
        print(f" Color: {self._color}")
        if self._is_bloom:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._has_shade = False

    def produce_shade(self):
        if not self._has_shade:
            print(f"[asking the {self._name} to produce shade]")
            print(
                f"Tree {self._name} now produces a shade of "
                f"{self._height:.1f}cm long and "
                f"{self._trunk_diameter}cm wide."
            )

    def show(self):
        super().show()
        print(f" Trunk diameter: {self._trunck_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self, name, height, age,
        harvest_season, nutritional_value=0, growth_rate=2.1
    ):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value
        self._growth_rate = growth_rate

    def show(self):
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def age(self, value):
        self._age += value
        self._grow(value)

    def grow(self, value):
        self._height += value * self._growth_rate
