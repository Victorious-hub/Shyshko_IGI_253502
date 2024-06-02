import time
import typing

def timing_average(func):
    """Custom timer function

    Args:
        func (_type_): any function
    """
    def wrapper(x, y):
        t0 = time.time_ns()
        res = func(x, y)
        t1 = time.time_ns()
        print(f"Execution time: {(t1 - t0) / 1e6} ms")
        return res

    return wrapper


def validate_input(num_type: type) -> list:
    """Check if the input is a number

    Args:
        num_type (type): type of the number

    Returns:
        list: just a list
    """
    while True:
        try:
            lst = list(map(num_type, input("Input array elements: ").split()))
            return lst
        except ValueError:
            print("Invalid input. Please try again.")   

def sequence_generator(start, end):
    """Generate a sequence of numbers

    Args:
        start (int): start of the sequence
        end (int): end of the sequence

    Yields:
        int: next number in the sequence
    """
    current = start
    while current <= end:
        yield current
        current += 1
    
def sequence_generator_input(num_type: int | float):
    """Generate a sequence of numbers based on user input

    Args:
        num_type (int | float): type of the number

    Yields:
        int | float: next number in the sequence
    """
    size = int(input("Enter the size of the sequence: "))
    it = 0
    while it <= size:
        inp = num_type(input("Enter the next number: "))
        yield inp
        it += 1


def custom_factorial(x: int) -> int:
    """Calculate the factorial of a number

    Args:
        x (int): number

    Returns:
        int: factorial of x
    """
    if x == 0 or x == 1:
        return 1
    return x * custom_factorial(x - 1)