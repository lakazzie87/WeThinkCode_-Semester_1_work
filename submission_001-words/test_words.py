import unittest
#import sys
#from test_word_processor import run_unittests
import word_processor

class MyTestCase(unittest.TestCase):

    def test_split(self):
        text = "Lekau is a dumb,dumb hello. world"
        delimiters = ",?:;. "
        result = ["Lekau","is","a","dumb","dumb","hello","","world"]
        self.assertEqual(word_processor.split(delimiters, text),result)

    def test_convert_to_word_list(self):
        text = "Lekau is a dumb,dumb hello. world"
        result = ["lekau","is","a","dumb","dumb","hello","world"]
        self.assertEqual(word_processor.convert_to_word_list(text),result)

    def test_word_longer_than(self):
        text = "these are indeed interesting an obvious understatement times what say you"
        result = ['interesting', 'understatement']
        self.assertEqual(word_processor.words_longer_than(10,text),result)

    def test_words_lengths_map(self):
        text = "these are indeed interesting an obvious understatement times what say you"
        result = {2: 1, 3: 3, 4: 1, 5: 2, 6: 1, 7: 1, 11: 1, 14: 1}
        self.assertEqual(word_processor.words_lengths_map(text),result)

    def test_letters_count_map(self):
        text = "these are indeed interesting an obvious understatement times what say you"
        result = {'a': 5, 'b': 1, 'c': 0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0}
        self.assertEqual(word_processor.letters_count_map(text),result)

    def test_most_used_character(self):
        text = "these are indeed interesting an obvious understatement times what say you"
        result = 'e'
        self.assertEqual(word_processor.most_used_character(text),result)
