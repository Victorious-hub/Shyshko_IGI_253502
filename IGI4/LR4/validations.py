def validate_integer() -> int:
    while True:
        try:
            var = int(input("Input any int: "))
            return var
        except ValueError:
            print("Type is incorrect")
            continue

def validate_float() -> int:
    while True:
        try:
            var = float(input("Input any float: "))
            return var
        except ValueError:
            print("Type is incorrect")
            continue
    