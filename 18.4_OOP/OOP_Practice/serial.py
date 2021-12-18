class SerialGenerator:
    '''Creates a number generator'''
    def __init__(self,start=0):
        '''Initializes number generator from a start num'''
        n = start;
        self.start = start;
        self.n = n
    def __repr__(self):
        return f'SerialGenerator(start={self.start}, number={self.n})'
    def generate(self):
        self.n += 1;
        return self.n;
    def reset(self):
        self.n = self.start;
        return self.n;