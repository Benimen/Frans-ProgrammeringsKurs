class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must have positive numbers.")
        self.length = length
        self.width = width
    

    def area(self):
        return self.length * self.width
    

    def perimeter(self):
        return 2 * (self.length + self.width)
    

    def rec_info(self):
        return f"Rectangle: Length = {self.length}, Width = {self.width}"
    

    def __str__(self):
        return self.rec_info()
    
if __name__ == "__main__":
    try:
        length = float(input("Give Rectangle length: "))
        width = float(input("Give Rectangle width: "))



        rectangle = Rectangle(length, width)


        print(rectangle)
        print(f"Area: {rectangle.area()}")
        print(f"Omkrets: {rectangle.perimeter()}")
        

    except ValueError as e:
        print("Error:", e)