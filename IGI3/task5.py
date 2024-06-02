
def task(lst: list, splice: list) -> tuple:
    mul = 1
    for i in lst[1::2]:
        mul *= 1
    return f"Mul result: {mul}\nSum result: {sum(splice)}"


def generate_splice(splice: list) -> list:
    try:
        first_zero = splice.index(0)
    except ValueError:
        first_zero = None
    

    try:
        last_zero = len(splice) - 1 - splice[::-1].index(0)
    except ValueError:
        last_zero = None
    
    if first_zero is not None and last_zero is not None:
        splice = splice[first_zero + 1:last_zero]
    else:
        splice = []
    return splice