class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = float(height)
        self.age = age

    def show(self):
        print(
            f"Created: {self.name}: "
            f"{round(self.height, 1)}cm, "
            f"{self.age} days old"
        )


def ft_plant_factory():
    print("=== Plant Factory Output ===")

    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]

    for plant in plants:
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
