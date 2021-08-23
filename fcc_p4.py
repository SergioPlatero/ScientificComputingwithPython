###CREATE RECTANGLE CLASS###
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def set_width(self, width):
        """
        Setter for width.
        """
        self.width = width

    def set_height(self, height):
        """
        Setter for height.
        """
        self.height = height

    def get_area(self):
        """
        Returns Area of Rectangle (Width*Height)
        """
        return (self.width*self.height)

    def get_perimeter(self):
        """
        Returns Perimeter of Rectangle (2*Width + 2*Height)
        """
        return ((2*self.width) + (2*self.height))

    def get_diagonal(self):
        """
        Returns Diagonal of Rectangle
        ((width**2)+(height**2))**.5
        """

        return ((self.width**2)+(self.height**2))**.5

    def get_picture(self):
        """
        Returns a 'picture' of the Rectangle in '*' characters.
        """

        if (self.width > 50) or (self.height > 50):
            return "Too big for picture."
        
        picture = ""
        
        for line in range(self.height):
            picture += "*"*self.width
            picture += "\n"

        return picture


    def get_amount_inside(self, other):
        """
        Takes another shape (square or rectangle) as an argument.
        Returns the number of times the passed in shaped could fit inside
        the shape (with no rotations.

        For instance, a rectoange with a width of 4 and height of 8 could fit
        in two squares with sides of 4.
        """
        num = 0
        outside = self.get_area()
        inside = other.get_area()

        num = outside//inside
        
        return num

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):

    def __init__(self, size):
        self.width = size
        self.height = size
        self.side = size

    def set_side(self, size):
        self.side = size
        self.width = size
        self.height = size

    def set_width(self, size):
        return self.set_side(size)

    def set_height(self, size):
        return self.set_side(size)

    def __str__(self):
        return f"Square(side={self.side})"
        

    


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
 
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
 
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))










