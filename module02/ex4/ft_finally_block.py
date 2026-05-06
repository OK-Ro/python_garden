class GardenError(Exception):
    def __init__(self, message = "Unknown garden error"):
        super().__init__(message)

def water_plant(plant_name):
    capitalized = plant_name.capitalize()
    if plant_name != capitalized:
        print("Not capilized")
        # raise PlantError("Caught PlantError:")
    else:
        print(f"Watering {capitalized}: [OK]")
        
if __name__ == "__main__":
    water_plant("Banana")