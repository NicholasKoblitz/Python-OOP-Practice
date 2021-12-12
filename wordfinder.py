"""Word Finder: finds random words from a dictionary."""
from random import randint


class WordFinder:
    """ Reads a list of words from the given text file and converts it into a list object"""

    def __init__(self, path):
        self.path = path
        self.word_lst = []
        self.get_file()

    def get_file(self):
        """ Gets the words in the file and creates a list out of the words"""
        file = open(self.path)
        for line in file:
            clean_line = line.rstrip()
            self.word_lst.append(clean_line)
        print(f"{len(self.word_lst)} words read")
        file.close()

    def random(self):
        """Returns a random word from the read file"""
        rand_int = randint(0, len(self.word_lst))
        return self.word_lst[rand_int]


class SpecialWordFinder(WordFinder):
    """A subclass of WordFinder that is used when a file has special characters like # or empty lines"""

    def __init__(self, path):
        super().__init__(path)

    def get_file(self):
        """Returns on the lines that have not soecial characters or empty lines"""
        with open(self.path, "r") as file:
            for line in file:
                clean_line = line.rstrip()
                if clean_line != "#" and clean_line:
                    self.word_lst.append(clean_line)
