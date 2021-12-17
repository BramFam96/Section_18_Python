def print_uppercase_words(words):
    '''Accepts a list of words and capitalizes them'''
    for word in words:
        print(word.upper());
def print_some_uppercase_words (words):
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper());
def print_specific_uppercase_words (words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper());
    return;            