class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def test_plant_error():
    raise PlantError("The tomato plant is wilting!")


def test_water_error():
    raise WaterError("The tomato plant is wilting!")


def ft_custom_errors():
    print("=== Custom Garden Errors Demo ===")
    print()

    print("Testing PlantError...")
    try:
        test_plant_error()
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print()

    print("Testing WaterError...")
    try:
        test_water_error()
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print()

    print("Testing catching all garden errors...")
    try:
        test_plant_error()
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    try:
        test_water_error()
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
