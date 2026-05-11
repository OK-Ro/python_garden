import sys

print("=== Inventory System Analysis ===")

args = sys.argv[1:]

inventory = {}

for arg in args:
    if ":" not in arg:
        print(f"Error - invalid parameter '{arg}'")
        continue

    item, quantity = arg.split(":")

    try:
        qty = int(quantity)
    except ValueError as error:
        print(f"Quantity error for '{item}': {error}")
        continue

    if item in inventory:
        print(f"Redundant item '{item}' - discarding")
    else:
        inventory[item] = qty

# --------------------------
# DISPLAY INVENTORY
# --------------------------
print(f"Got inventory: {inventory}")

items = list(inventory.keys())
print(f"Item list: {items}")

total = sum(inventory.values())
print(f"Total quantity of the {len(inventory)} items: {total}")


# PERCENTAGES
for item, qty in inventory.items():
    percentage = (qty / total) * 100
    print(f"Item {item} represents {round(percentage, 1)}%")


# MOST / LEAST ABUNDANT
most_item: str = next(iter(inventory))
least_item: str = next(iter(inventory))

for item, qty in inventory.items():
    if most_item is None or qty > inventory[most_item]:
        most_item = item

    if least_item is None or qty < inventory[least_item]:
        least_item = item

print(f"Item most abundant: {most_item} with quantity {inventory[most_item]}")
print(f"Item least abundant: {least_item} with quantity {inventory[least_item]}")

# UPDATE INVENTORY
inventory.update({"magic_item": 1})
print(f"Updated inventory: {inventory}")
