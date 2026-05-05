def garden_operations(operation_number):
    if operation_number == 0:
        return int("abc")

    elif operation_number == 1:
        return 10 / 0

    elif operation_number == 2:
        open("/non/existent/file.txt", "r")

    elif operation_number == 3:
        return "10" + 5

    else:
        return "Operation completed successfully"


def test_error_types():
    print("=== Garden Error Types Demo ===")
    print()

    print("Testing operation 0...")
    try:
        garden_operations(0)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print()

    print("Testing operation 1...")
    try:
        garden_operations(1)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print()

    print("Testing operation 2...")
    try:
        garden_operations(2)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    print()

    print("Testing operation 3...")
    try:
        garden_operations(3)
    except TypeError as e:
        print(f"Caught TypeError: {e}")
    print()

    print("Testing operation 4...")
    try:
        print(garden_operations(4))
    except Exception as e:
        print(f"Caught unexpected error: {e}")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
