class Plant:
    class Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self):
            print(
                f"Stats: {self.grow_calls} grow, "
                f"{self.age_calls} age, {self.show_calls} show"
            )

    def __init__(self, name, height, age):
        self.name = name
        self.height = float(height)
        self.age = age
        self._stats = self.Stats()

    def grow(self, growth_amount):
        self.height += growth_amount
        self._stats.grow_calls += 1

    def age_plant(self, days):
        self.age += days
        self._stats.age_calls += 1

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")
        self._stats.show_calls += 1

    @staticmethod
    def is_older_than_year(age_days):
        if age_days < 365:
            print(f"Is {age_days} days more than a year? -> False")
        else:
            print(f"Is {age_days} days more than a year? -> True")

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def display_stats(self):
        self._stats.display()


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.has_bloomed = False

    def bloom(self):
        self.has_bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")

        if self.has_bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self.shade_calls = 0

        def display(self):
            super().display()
            print(f"{self.shade_calls} shade")

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._stats = self.Stats()

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and "
            f"{self.trunk_diameter}cm wide."
        )
        self._stats.shade_calls += 1

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


def display_plant_statistics(plant):
    print(f"[statistics for {plant.name}]")
    plant.display_stats()


def ft_garden_analytics():
    print("=== Garden statistics ===")

    # CHECK YEARS
    print("\n=== Check year-old")
    Plant.is_older_than_year(30)
    Plant.is_older_than_year(400)

    # FLOWER
    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_plant_statistics(rose)

    # TREE
    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_statistics(oak)

    # SEED
    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age_plant(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_statistics(sunflower)

    # ANONYMOUS
    print("\n=== Anonymous")
    plant = Plant.anonymous()
    plant.show()
    display_plant_statistics(plant)


if __name__ == "__main__":
    ft_garden_analytics()
