#Py OOP
    # starts with keyword class like JS;
    # Py uses a syntax similar to a constructor, and self instead of this. 
from math import sqrt
from random import randint


class Triangle:
    '''Makes Right triangles'''
    # JS constructor is replaced with a dunder method, typically named init;
    # This init method is automatically called when a triangle is initialized;
    # All regular methods in class are passed the instance obj;
    def __init__(self,a,b):    
    # Self is not automatically created. Instead, it is included in our init, and
    # in any subsequent instance methods:
        '''Initializes triangle with side a and b'''
        self.a = a;
        self.b = b;
    def get_hypo(self):
        '''Calculates hypotenuse'''
        return sqrt(self.a **2 + self.b**2)
    def get_area(self):
        '''Calculates area'''
        return (self.a*self.b*0.5);
    def structure(self):
        '''Describes the triangle instance'''
        return f'Triangle with sides: {self.a}, {self.b}, and {self.get_hypo()}'
# All of the funcs above are instance methods, b/c they are called on, and bound to new vals by 
# the instance we create from this class;

# Class methods:
    # Far less common than instance methods
    # A common example is an instance generator: A method for instantiating a random triangle;
    # We define class methods with @classmethod: this changes the behavior of Py
    # NOTE classmethods are passed the class itself, not the instance. 
    @classmethod
    def random(cls):
        return cls(randint(1,10),randint(1,10))




