class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = float(height)
        self.age = age
        self.start_height = self.height

    def grow(self):
        self.height += 0.8

    def age_up(self):
        self.age += 1

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


def ft_plant_growth():
    rose = Plant("Rose", 25.0, 30)

    print("=== Garden Plant Growth ===")

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age_up()
        rose.show()

    total_growth = round(rose.height - rose.start_height, 1)
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
