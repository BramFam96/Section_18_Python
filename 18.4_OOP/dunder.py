from classes import Triangle;
# dunder methods are signified by double underscores: __init__;
# there are quite a few of them which allow us to customize py's
# default behavior in a number of ways 

# First we'll look at __repr__:
    # Let's say we have an instance of some class:
t = Triangle(3,4);
# When we log this class we get a message like: <__main__.Triangle ....>
# which contains no relevent information;
# It would be much nicer to see the data we've passed in, like a = 3 or b = 4;
# This is what repr allows us to do.
class New_T(Triangle):
    def __init__(self,a,b):
        super().__init__(a,b);
# NOTE repr doesn't need to be called, like init it's modifying py's behavior
# we simply make a new t t=New_T(3,4); and type t in the console.    
    def __repr__(self):
        return super().__repr__(self);
# We can change how == behaves with __eq__:
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b;

    
