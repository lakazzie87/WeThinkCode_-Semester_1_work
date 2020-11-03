import unittest
import super_algos

class Practice(unittest.TestCase):
    
    """ TO DO: test function for find_min. """
    def test_find_min(self):
        self.assertEqual(super_algos.find_min([]), -1)
        self.assertEqual(super_algos.find_min([1, 't', 'm', 4]), -1)
        self.assertEqual(super_algos.find_min([53, 3, 19, 6]), 3)


    """ TO DO: test function for sum_all. """
    def test_sum_all(self):
        self.assertEqual(super_algos.sum_all([]), -1)
        self.assertEqual(super_algos.sum_all([1,2,3,4]), 10)
        self.assertEqual(super_algos.sum_all(['z', 5, 8, 'e']), -1)


    """ TO DO: test function for find_possible_strings. """
    def test_find_possible_strings(self):
        output = ['xxx', 'xxy', 'xxz', 'xyx', 'xyy', 'xyz', 'xzx', 'xzy', 'xzz', 'yxx', 'yxy', 'yxz', 'yyx', 'yyy', 'yyz', 'yzx', 'yzy', 'yzz', 'zxx', 'zxy', 'zxz', 'zyx', 'zyy', 'zyz', 'zzx', 'zzy', 'zzz']
        self.assertEqual(super_algos.find_possible_strings([1,2,3,4], 3),[])
        self.assertEqual(super_algos.find_possible_strings(['z', 5, 3, 'c'], 3), [])
        self.assertEqual(super_algos.find_possible_strings(['x', 'y', 'z'], 3), output)
        self.assertEqual(super_algos.find_possible_strings([], 3), [])


if __name__ == "__main__":
    unittest.main()