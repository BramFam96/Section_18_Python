import random

class WordFinder:
    '''Finds, counts, and lists words from a text file
    >>> w = WordFinder('18.4_OOP/OOP_Practice/words.txt')
        4 words read
    '''
    

    def __init__(self,path):
        '''Initializes the finder with a path and makes the word list'''
        
        word_file = open(path, 'r')
        self.path = path;
        self.words = self.parse(word_file)
        print(f'{len(self.words)} words read')
    def __repr__(self):
        return f'WordFinder(path={self.path}, words = {self.words})'

    def parse(self, word_file):
        '''Strips white-space from words before they are added to list'''
        return [word.strip() for word in word_file]
    
    def random(self):
        '''returns a random word from the list'''
        return random.choice(self.words);

class SpecialWordFinder(WordFinder):
    '''Finds, counts, and lists words from a file - excluding comments and blank lines
     >>> sw = WordFinder('18.4_OOP/OOP_Practice/words.txt')
         3 words read
    '''
    def parse(self, word_file):
        '''parse out the words w/o including blank lines or comments'''
        return [word.strip() for word in word_file 
        if len(word.strip()) != 0 and not word.startswith('#')];
