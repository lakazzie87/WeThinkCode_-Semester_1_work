import unittest
#from mastermind import *
import mastermind
#import mock
from unittest.mock import patch
import sys
from io import StringIO

class create_code(unittest.TestCase):
    
    #return: tests computer generated code.

    def test_create_code(self):
        result = mastermind.create_code()
        self.assertTrue(result)


    #return: tests shows the instructions to user.

    def test_show_instructions(self):
        result = mastermind.show_instructions()
        self.assertEqual(print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it."), result)


    #return: test the result of 1 turn.
    
    def test_show_results(self):
        #output = StringIO()

        #sys.stdout = output

        #sys.stdout = sys.__stdout__

        result = True
        self.assertEqual(mastermind.check_correctness(8, 4), result)
                

    #return: tests the correctness of answer and show the output to user. 

    @patch("sys.stdin",StringIO("1234\n1234\n"))
    def test_check_correctness(self):
        self.assertEqual(mastermind.check_correctness(11, 4), True)
        self.assertEqual(mastermind.check_correctness(12, 4), True)

    
    #return: tests the logic of taking a turns including get answer from user, checks validiy, and check correckness of answer. 
    @patch("sys.stdin", StringIO("1234\n1234\n1234")) #String 1234 replaces stdin
    def test_take_turn(self):
        self.assertEqual(mastermind.take_turn([1, 2, 3, 4]),(4, 0))
        self.assertEqual(mastermind.take_turn([1, 2, 3, 7]),(3, 0))
        self.assertEqual(mastermind.take_turn([1, 3, 4, 5]),(1, 2))

if __name__ == '__main__':
    unittest.main()