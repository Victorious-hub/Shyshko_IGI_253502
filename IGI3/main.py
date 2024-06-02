"""Laboratory 3. In built data types, collections, functions, modules
Elborated by Shyshko Victor 253502 with python 3.10.12 version
"""

import math
from task1 import custom_asin, EPS
from task2 import find_max
from task3 import count_non_whitespace
from task4 import STRING, find_letter_z, upper_amount
from task5 import generate_splice, task
from utils import sequence_generator_input, validate_input

def main():
    while True:
        print("Choose and number from 1 to 5 choose tasks number\n")
        print("1. Custom asin function")
        print("2. Custom max in list")
        print("3. Count non whitespace")
        print("4. Analyze string")
        print("5. Task with list")

        task_number = input()
        match task_number:
            case "1":
                while True:
                    try:
                        x = float(input("Input any number: "))
                        if x > 1 or x < -1:
                            raise Exception
                    except Exception:
                        print("x should be in range [-1, 1] or nit correct type")
                        continue
                    
                    result = custom_asin(x, EPS)
                    print(
                        f"n = {result[0]}\nx = {x}\nF(x) = {result[1]}\nMath(F(x)) = {math.asin(x)}\neps = {EPS}" 
                    )
                    break
            case "2":
                while True:
                    print(
                        f"Choose the way of generation of list\n(1) User input\n(other) Custom generator"
                    )
                    try:
                        choice = int(input())
                    except ValueError:
                        print("Invalid input! Try again")
                    
                    if choice == 1:
                        lst = validate_input(int)
                    else:
                        lst = list(sequence_generator_input(int))
                    print(find_max(lst))
                    break
            case "3":
                string = input("Input any string: ")
                print(count_non_whitespace(string))
            case "4":
                print(
                    f"Upper letters amount: {upper_amount(STRING)}\nfirst letter z in occurence: {find_letter_z(STRING)}"
                )
            case "5":
                while True:
                    print(
                        f"Choose the way of generation of list\n(1) User input\n(other) Custom generator"
                    )
                    try:
                        choice = int(input())
                    except ValueError:
                        print("Invalid input! Try again")
                    
                    if choice == 1:
                        lst = validate_input(int)
                    else:
                        lst = list(sequence_generator_input(int))
                    splice = generate_splice(lst)
                    print(f"List output:{lst}\nSolving task:{task(lst, splice)}")

                    break
            case "0":
                print("Goodbye!")
                exit(1)
            case _:
                print("It's wrong. Just try again")
                continue
        
        continue_or_exit = input("Do you want to continue? (yes/no): ")
        if continue_or_exit.lower() != "yes":
            break

if __name__ == "__main__":
    main()