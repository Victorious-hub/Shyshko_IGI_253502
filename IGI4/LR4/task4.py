import math
import matplotlib.pyplot as plt
import numpy as np
from abstractions import GeometricFigure
from validations import validate_float, validate_integer


class FigureColor:
    COLORS = {
        "w": "white",
        "g": "green",
        "b": "blue",
        "y": "yellow"
        }
    def __init__(self, color: str=None):
        self.__color = color
    
    @property
    def color_ch(self):
        return self.__color
    
    @color_ch.setter
    def color_ch(self, color):
        self.__color = color

class Hexagon(GeometricFigure):
    DIR_NAME = "media/task4"
    N = 6
    FIGURE_NAME = "Hexagon"

    def __init__(self, side_length: int):
        self.__side_length = side_length
        self.obj_color = FigureColor()
    
    @classmethod
    def get_figure_name(cls):
        """Function to get figure name

        Returns:
            _type_: str
        """
        return f"Figure name: {cls.FIGURE_NAME}" 

    @property
    def get(self):
        return self.__side_length
    
    @get.setter
    def get(self, side_length):
        self.__side_length = side_length
    
    def area(self):
        """Function to calculate hexagon's area

        Returns:
            _type_: str
        """
        return f"Area: {3*math.sqrt(3)*math.pow(self.__side_length,2)/2}"
    
    def __str__(self):
        return f"Figure name: {self.get_figure_name()}\nside: {self.__side_length}\nSide amount: {self.N}"
    
    def plot_hexagon(self):
        """Function to plot hexagon
        """
        theta = np.linspace(0, 2*np.pi, self.N+1)

        x = self.__side_length * np.cos(theta)  
        y = self.__side_length * np.sin(theta)  

        plt.figure()
        plt.plot(x, y, linewidth=2)
        color = str(self.obj_color.color_ch)
        plt.fill(x, y, color)  
        plt.axis('equal')
        plt.title(self.FIGURE_NAME)

        plt.savefig(f"{self.DIR_NAME}/hexagon.jpg")
        plt.show()
        
def task4(): 
    side = validate_float()
    is_breaked = False
    obj = Hexagon(side)
    while True:
        print("---------------------------------------")
        step = int(input("Other steps:\n1. Calculate hexagon's area\n2. Plot hexagon\n3. Output class data\n4. Change side len\n5. Change figure color\n6. Exit\n"))
        print("---------------------------------------")
        match step:
            case 1:
                print(obj.area())
            case 2:
                obj.plot_hexagon()
            case 3:
                print(obj)
            case 4:
                new_side = validate_integer()
                obj.get = new_side
            case 5:
                color = input(f"Change color: {FigureColor.COLORS}: ")
                obj.obj_color.color_ch = color
            case 6:
                is_breaked = True
                break
            case _:
                print("Wtf are you doing here?")
        if is_breaked:
            break
        continue
