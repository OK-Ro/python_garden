class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def water_plant(plant_name):
    capitalized = plant_name.capitalize()

    if plant_name != capitalized:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")

    print(f"Watering {capitalized}: [OK]")


def test_watering_system():
    print("=== Garden Watering System ===")
    print()

    # ---------------- VALID TEST ----------------
    print("Testing valid plants...")
    print("Opening watering system")

    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")

    except PlantError as error:
        print(f"Caught PlantError: {error}")

    finally:
        print("Closing watering system")
        print()

    # ---------------- INVALID TEST ----------------
    print("Testing invalid plants...")
    print("Opening watering system")

    try:
        water_plant("tomato")
        water_plant("lettuce")
        water_plant("carrots")

    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
        return

    finally:
        print("Closing watering system")
        print()

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
