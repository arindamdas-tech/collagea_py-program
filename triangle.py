import math

# Parent class
class Triangle:
    def __init__(self, side1, side2, side3, angle1, angle2, angle3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3


# Child class
class EquilateralTriangle(Triangle):

    def cal_area(self):
        # Area of equilateral triangle = sqrt(3)/4 * side^2
        return (math.sqrt(3) / 4) * self.side1 ** 2

    def find_angle(self):
        tan1 = math.tan(math.radians(self.angle1))
        tan2 = math.tan(math.radians(self.angle2))
        tan3 = math.tan(math.radians(self.angle3))

        print("tan(angle1) =", tan1)
        print("tan(angle2) =", tan2)
        print("tan(angle3) =", tan3)


# Creating object
side = float(input("Enter side of equilateral triangle: "))

triangle = EquilateralTriangle(
    side, side, side,
    60, 60, 60
)

print("Area of Equilateral Triangle =", triangle.cal_area())

triangle.find_angle()