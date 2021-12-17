# Class inheritance:
    # Let's extend the triangle class from classes.py;
from classes import Triangle;

# Rather than use extend, we pass our original class into our new one
class Colored_Triangle(Triangle):
    'Makes colored right triangles'
    # In JS super refers to our parent; super() refers to our parent's constructor func;
    # In Py super() refers to our parent; super().__init__(...)
    def __init__(self, a,b, color):
        'Initializes a colored triangle with side a, b, and a color'
#we do not need to pass self to our parent constructor; 
        super().__init__(a,b);
        self.color = color;
# we can override inheritted methods by modifying them directly:
    def structure(self):
        'Describes the structure of a colored triangle instance'
        msg = super().structure()
        return f'A {self.color} {msg}'
    
