import unittest
import robot
from io import StringIO 
from unittest.mock import patch
import sys

class Robot_moving(unittest.TestCase):
    @patch("sys.stdin", StringIO("el\noff\n"))
    def test_name_the_robot(self):
        with patch("sys.stdout",new=StringIO()) as var:
            robot.robot_start()
            output = var.getvalue().strip()
            self.assertEqual(output,"""What do you want to name your robot? el: Hello kiddo!
el: What must I do next? el: Shutting down..""")

    @patch("sys.stdin", StringIO("el\noff\n"))
    def test_get_command(self):
        with patch("sys.stdout",new=StringIO()) as var:
            robot.robot_start()
            output = var.getvalue().strip()
            self.assertEqual(output,"""What do you want to name your robot? el: Hello kiddo!
el: What must I do next? el: Shutting down..""")

if __name__ == "__main__":
    unittest.main()