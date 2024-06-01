from task1 import task1
from task2 import task2
from task3 import task3
from task4 import task4
from task5 import task5

"""Laboratory Work 4. 
"""


def main():
    """Main function to choose any task
    """
    while True:
        print("Choose any task")
        print("1.Working with files")
        print("2.Text analyse")
        print("3.Custom function task")
        print("4.Figures task")
        print("5.Numpy task")
        inp = int(input("Input any number from 1 to 5: "))
        match inp:
            case 1:
                task1()
            case 2:
                task2()
            case 3:
                task3()
            case 4:
                task4()
            case 5:
                task5()
            case _:
                print("Something wen wrong. Try again")
        step = int(input("If you wanna exit, input 0: "))
        if step == 0:
            break
        else:
            continue

if __name__ == "__main__":
    main()