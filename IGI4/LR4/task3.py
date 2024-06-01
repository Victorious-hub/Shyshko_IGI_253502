import math
import matplotlib.pyplot as plt
from statistics import StatisticsError

import numpy as np

from validations import validate_float


class AsinCalculation:
    EPS = 1e-10
    DIR_NAME = "media/task3"

    def __init__(self, x: float | int):
        self.x = x
        self.seq = list()

    def custom_factorial(self, x: int) -> int:
        """Function to calculate factorial of a number

        Args:
            x (int): number to calculate factorial

        Returns:
            int: factorial of a number
        """
        if x == 1 or x == 0:
            return 1
        else:
            return x * self.custom_factorial(x - 1)

    def calculate_asin(self) -> float | int:
        """Function to calculate asin(x) using Taylor series

        Returns:
            float | int: tuple with n and result
        """
        result = 0
        prev_result = 0

        for n in range(500):
            result += self.custom_factorial(2 * n) / (
                self.custom_factorial(n) ** 2 * 4**n * (2 * n + 1)) * self.x**(2 * n + 1)
            self.seq.append(result)
            if abs(result - prev_result) < self.EPS:
                break
            prev_result = result

        return (n, result,)

    def custom_mean(self):
        """Function to calculate mean of a list

        Returns:
            _type_: str
        """
        return f"Mean of seq elements: {sum(1 for i in self.seq) / len(self.seq)}"

    def custom_median(data):
        """Return the median (middle value) of numeric data.

        When the number of data points is odd, return the middle data point.
        When the number of data points is even, the median is interpolated by
        taking the average of the two middle values:
        """
        data = sorted(data)
        n = len(data)
        if n == 0:
            raise StatisticsError("no median for empty data")
        if n % 2 == 1:
            return data[n // 2]
        else:
            i = n // 2
            return (data[i - 1] + data[i]) / 2

    def custom_mode(self):
        """Function to find most frequent element in a list

        Returns:
            _type_: list
        """
        most = max(list(map(self.seq.count, self.seq)))
        return list(set(filter(lambda x: self.seq.count(x) == most, self.seq)))

    def custom_variance(self):
        """Function to calculate variance of a list

        Returns:
            _type_: 
        """
        n = len(self.seq)
        if n < 2:
            return None

        mean = sum(self.seq) / n
        variance = sum((x - mean) ** 2 for x in self.seq) / (n - 1)
        return variance

    def custom_std(data):
        """Return the sample standard deviation of data.

        Args:
            data (_type_): list of data

        Returns:
            _type_: float
        """
        n = len(data)
        if n < 2:
            return None

        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / (n - 1)
        std = math.sqrt(variance)
        return std
    
    def build_custom_asin(self):
        """Function to build custom asin(x) function
        """
        x_values = range(len(self.seq))
        fig, ax = plt.subplots(figsize=(8, 4))

        ax.plot(x_values, self.seq, marker='o', linestyle='-', color='b', label='Custom asin(x) function')
        
        y_values = np.arcsin(x_values)
        ax.plot(x_values, y_values, marker='o', linestyle='-', color='r', label='Numpy arcsin(x) function')

        plt.legend()
        plt.savefig(f"{self.DIR_NAME}/asin.jpg")
        plt.tight_layout()
        plt.show()


def task3():
    num = validate_float()
    is_breaked = False
    obj = AsinCalculation(num)
    while True:
        print("---------------------------------------")
        step = int(input("Other steps:\n1. Calculate custom asin\n2. Custom median fucntion\n3. Custom mode fucntion\n4. Custom std fucntion\n5. Custom var fucntion\n6. Exit\n"))
        print("---------------------------------------")
        match step:
            case 1:
                print(obj.calculate_asin())
                print(obj.build_custom_asin())
            case 2:
                print(obj.custom_median())
            case 3:
                print(obj.custom_mode())
            case 4:
                print(obj.custom_std())
            case 5:
                print(obj.custom_variance())
            case 7:
                is_breaked = True
                break
            case _:
                print("Wtf are you doing here?")
        if is_breaked:
            break
        continue

