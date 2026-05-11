# An exception is an event that interrupts the normal flow of a program.
# Common examples: ZeroDivisionError, TypeError, ValueError, SyntaxError
#
# Basic exception handling structure:
# 1. try     -> code that might raise an exception
# 2. except  -> handles the exception if one occurs


def input_temperature(temp_str):
    return int(temp_str)

inputs = ["abc", "25"]


def test_temperature():
    print("=== Garden Temperature ===")
    print()

    for x in inputs:
        print (f"input is {x}")
        try:
            print(f"Temperature is now {input_temperature(x)}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    # test 1: valid input
    # print("Input data is '25'")
    # try:
    #     temp = input_temperature("25")
    #     print(f"Temperature is now {temp}°C")

    # except ValueError as e:
    #     print(f"Caught input_temperature error: {e}")

    # print()

    # # test 2: invalid input
    # print("Input data is 'abc'")
    # try:
    #     temp = input_temperature("abc")
    #     print(f"Temperature is now {temp}°C")
    # except ValueError as e:
    #     print(f"Caught input_temperature error: {e}")

    # print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
