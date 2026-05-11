import math


def get_player_pos():
    while True:
        user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
        coordinates = user_input.split(",")

        if len(coordinates) != 3:
            print("Invalid syntax")
            continue

        current_coord = []

        for cordinate in coordinates:
            cordinate = cordinate.strip()
            try:
                current_coord.append(float(cordinate))
            except ValueError as error:
                print(f"Error on parameter '{cordinate}': {error}")
                break
        else:
            return tuple(current_coord)


print("=== Game Coordinate System ===")

print("Get a first set of coordinates")
pos1 = get_player_pos()

print(f"Got a first tuple: {pos1}")
print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

first_distance = math.sqrt(pos1[0] ** 2 + pos1[1] ** 2 + pos1[2] ** 2)
print(f"Distance to center: {round(first_distance, 4)}")

print("Get a second set of coordinates")
pos2 = get_player_pos()

second_distance = math.sqrt(
    (pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2 + (pos2[2] - pos1[2]) ** 2
)

print(f"Distance between the 2 sets of coordinates: {round(second_distance, 4)}")
