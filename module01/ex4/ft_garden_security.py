class Plant:
    def __init__(self, name, height, age):
        self.name = name

        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = float(height)

        if age < 0:
            print(f"{name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def set_height(self, new_height):
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(new_height)
            print(f"Height updated: {new_height}cm")

    def set_age(self, new_age):
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {new_age} days")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def show(self):
        print(
            f"Plant created: {self.name}: "
            f"{round(self._height, 1)}cm, "
            f"{self._age} days old"
        )


def ft_garden_security():
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    rose.show()

    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-8)
    rose.set_age(-20)

    print(
        f"Current state: {rose.name}: "
        f"{round(rose.get_height(), 1)}cm, "
        f"{rose.get_age()} days old"
    )


if __name__ == "__main__":
    ft_garden_security()
