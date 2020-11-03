import robot
import unittest
from unittest.mock import patch
from io import StringIO
import sys

class robot3(unittest.TestCase):
  

            
    def test_history(self):
        self.assertEqual(robot.history("forward 5", ['back 7']), ['back 7','forward 5'])
        
        
    @patch("sys.stdin", StringIO("forward 10"))
    def test_split_command_input(self):
        with patch ("sys.stdout", new=StringIO()) as var:
            robot.split_command_input("forward 10")
            output = var.getvalue().strip()
            self.assertEqual(output, """""")


    @patch("sys.stdin", StringIO("forward 10"))
    def test_valid_command(self):
        with patch ("sys.stdout", new=StringIO()) as var:
            robot.valid_command("forward 10")
            output = var.getvalue().strip()
            self.assertEqual(output, """""")
            
            
    @patch("sys.stdin", StringIO("el\nreplay"))
    def test_handle_command(self):
        with patch ("sys.stdout", new=StringIO()) as var:
            robot.handle_command("el", "replay")
            output = var.getvalue().strip()
            self.assertEqual(output, """> el replayed 0 commands.
> el now at position (0,0).""")
            
            
    @patch("sys.stdin", StringIO("forward 10"))
    def test_valid_command(self):
        with patch ("sys.stdout", new=StringIO()) as var:
            robot.valid_command("forward 10")
            output = var.getvalue().strip()
            self.assertEqual(output, """""")
            
            
    @patch("sys.stdin", StringIO("el\nforward 3\nforward 2\nforward 1\nreplay silent\noff"))
    def test_handle_command(self):
        with patch ("sys.stdout", new=StringIO()) as var:
            robot.robot_start()
            output = var.getvalue().strip()
            self.assertEqual(output, """What do you want to name your robot? el: Hello kiddo!
el: What must I do next?  > el moved forward by 3 steps.
 > el now at position (0,3).
el: What must I do next?  > el moved forward by 2 steps.
 > el now at position (0,5).
el: What must I do next?  > el moved forward by 1 steps.
 > el now at position (0,6).
el: What must I do next?  > el replayed 3 commands silently.
 > el now at position (0,12).
el: What must I do next? el: Shutting down..""")


    @patch("sys.stdin", StringIO("el\nforward 3\nforward 2\nforward 1\nreplay\noff"))
    def test_replay1(self):
        with patch ("sys.stdout", new=StringIO()) as var:
            robot.robot_start()
            output = var.getvalue().strip()
            self.maxDiff = None
            self.assertEqual(output, """What do you want to name your robot? el: Hello kiddo!
el: What must I do next?  > el moved forward by 3 steps.
 > el now at position (0,3).
el: What must I do next?  > el moved forward by 2 steps.
 > el now at position (0,5).
el: What must I do next?  > el moved forward by 1 steps.
 > el now at position (0,6).
el: What must I do next?  > el moved forward by 3 steps.
 > el now at position (0,9).
 > el moved forward by 2 steps.
 > el now at position (0,11).
 > el moved forward by 1 steps.
 > el now at position (0,12).
 > el replayed 3 commands.
 > el now at position (0,12).
el: What must I do next? el: Shutting down..""")
            
            
    @patch("sys.stdin", StringIO("el\nforward 3\nforward 2\nforward 1\nreplay reversed\noff"))
    def test_replay(self):
        with patch("sys.stdout", new=StringIO()) as var:
            robot.robot_start()
            output = var.getvalue().strip()
            self.maxDiff = None
            self.assertEqual(output, """What do you want to name your robot? el: Hello kiddo!
el: What must I do next?  > el moved forward by 3 steps.
 > el now at position (0,3).
el: What must I do next?  > el moved forward by 2 steps.
 > el now at position (0,5).
el: What must I do next?  > el moved forward by 1 steps.
 > el now at position (0,6).
el: What must I do next?  > el moved forward by 1 steps.
 > el now at position (0,7).
 > el moved forward by 2 steps.
 > el now at position (0,9).
 > el moved forward by 3 steps.
 > el now at position (0,12).
 > el replayed 3 commands in reverse.
 > el now at position (0,12).
el: What must I do next? el: Shutting down..""")
        
            
if __name__ == "__main__":
    unittest.main()