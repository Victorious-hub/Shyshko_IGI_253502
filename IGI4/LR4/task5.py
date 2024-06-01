from statistics import StatisticsError
import numpy as np

from validations import validate_integer

class NumpyUtils:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.np_array = np.random.randint(0, 100, (self.n, self.m)) 
    
    def custom_median(self, data):
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
    
  
    def calculate_median(self):
        """Function to calculate median of numpy array and custom median

        Returns:
            _type_: str
        """
        print(self.np_array[1])
        return f"Numpy median function: {np.median(self.np_array[1])}\n custom median: {self.custom_median(self.np_array[1])}"

    def insert_row(self):
        """Function to insert first row after the row with minimum value in numpy array
        """
        first_row = self.np_array[0]
        min_index = np.where(self.np_array == self.np_array.min())[0][0]
        self.np_array = np.insert(self.np_array, min_index + 1, first_row, axis=0)
        print(self.np_array)
    
    def __str__(self):
        return f"Matrix: {self.np_array}"
    
        

def task5():
    rows = validate_integer()
    cols = validate_integer()
    is_breaked = False
    obj = NumpyUtils(rows, cols)
    while True:
        print("---------------------------------------")
        step = int(input("Other steps:\n1. Calculate custom and in built function\n2. Insert first row after min elen in row before\n3. Exit\n"))
        print("---------------------------------------")
        match step:
            case 1:
                print(obj.calculate_median())
            case 2:
                obj.insert_row()
            case 3:
                is_breaked = True
                break
            case _:
                print("Wtf are you doing here?")
        if is_breaked:
            break
        continue
