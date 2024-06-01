from collections import defaultdict
import csv
import pickle
import pandas as pd
from fractions import Fraction

from validations import validate_integer
""" Task1. Variant 27. Imagine rational number as dictionary, where key is a numerator and the value is a denumerator 
а) find equal fractions
б) find the biggest fraction
"""
class FractionHandler:
    def __init__(self):
        self.fraction = dict()
        self.frac = defaultdict(int)
        self.tmp = dict()

    def get_fraction(self, numerator: int, denumerator: int):
        fraction_obj = Fraction(numerator, denumerator)
        self.frac[fraction_obj] += 1
    
    def add_fraction(self, numerator: str, denumerator: int):
        self.fraction[numerator] = denumerator
        self.get_fraction(self.fraction)
      
    def add_fraction(self, numerator: str, denumerator: int):
        self.fraction[numerator] = denumerator
        self.get_fraction(numerator, denumerator)

    def get_max(self):
        return f"Max fraction: {sorted(list(self.frac))[-1]}"
    
    def find_equal_fractions(self):
        for k,v in self.frac.items():
            if v > 1:
                print (f"Fraction: {k}, amount: {v}")
    
    def __str__(self):
        return f"{self.fraction}"


class CSVSerializer(FractionHandler):
    DIR_NAME = "media/task1"
    
    def __init__(self):
        super().__init__()
     
    def serialize(self):
        keys = list(self.fraction.keys())
        values = list(self.fraction.values())
        
        with open(f"{self.DIR_NAME}/fraction.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['numerator', 'denumerator'])
            writer.writerows(zip(keys, values))

    def deserialize(self):
        df = pd.read_csv(f"{self.DIR_NAME}/fraction.csv")
        print(df)
        with open(f"{self.DIR_NAME}/fraction.csv") as fp:
            reader = csv.reader(fp, delimiter=",", quotechar='"')
            next(reader)
            data_read = {row[0]: row[1] for row in reader}
        
        self.tmp = data_read

    def __str__(self):
        return f"{self.fraction}"


class PickleSerializer(FractionHandler):
    DIR_NAME = "media/task1"

    def __init__(self):
        super().__init__()
 
    def serialize(self):
        with open(f"{self.DIR_NAME}/fraction.pkl", "wb") as file:
            pickle.dump(self.fraction, file)

    def deserialize(self):
        with open(f"{self.DIR_NAME}/fraction.pkl", 'rb') as file:
            data = pickle.load(file)
        print(data)

    def __str__(self):
        return f"{self.fraction}"


def task1():
    obj = None
    is_breaked = False
    file_handler = int(input("Choose file handler:\n1. CSV\n2. Pickle "))
    obj = CSVSerializer() if file_handler == 1 else PickleSerializer()
    while True:
        print("---------------------------------------")
        step = int(input("Other steps:\n1. Add fraction\n2. Write in file\n3. Inspect file data\n4. Find max fraction\n5. Equal fractions\n6. Exit\n"))
        print("---------------------------------------")
        match step:
            case 1:
                enumerator = validate_integer()
                denumerator = validate_integer()
                obj.add_fraction(enumerator, denumerator)
            case 2:
                obj.serialize()
            case 3:
                obj.deserialize()
            case 4:
                print(obj.get_max())
            case 5:
                obj.find_equal_fractions()
            case 6:
                is_breaked = True
                break
            case _:
                print("Wtf are you doing here?")
        if is_breaked:
            break
        continue
    