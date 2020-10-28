import unittest
import robot
from unittest.mock import patch
from io import StringIO
import sys


class test_toy(unittest.TestCase):
    @patch("sys.stdin", StringIO("hel\noff\n"))
    def test_valid_input(self):
        self.assertEqual(robot.validate_command("sonni", "Help"),"Help")
        self.assertEqual(robot.validate_command("sonni", "help"),"help")
        self.assertEqual(robot.validate_command("sonni", "HELP"),"HELP")
        with patch("sys.stdout", new = StringIO()) as the_output:
            robot.validate_command("sonni", "of")
            self.assertEqual(the_output.getvalue().strip(),"""sonni: Sorry, I did not understand 'of'.
sonni: What must I do next? sonni: Sorry, I did not understand 'hel'.
sonni: What must I do next?""")


    def test_help_command(self):
        value = robot.execute_command("Usher", "help")
        self.assertEqual(value, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - moves the robot forward
BACK - moves robot back
RIGHT - turns the robot right
LEFT - turns robot left
SPRINT - makes the robot sprint""")


    @patch("sys.stdin", StringIO("Bond\nforward 5\noff"))
    def test_forward_command(self):
        with patch("sys.stdout", new = StringIO()) as the_output:
            robot.robot_start()
            self.assertEqual(the_output.getvalue(),"""What do you want to name your robot? Bond: Hello kiddo!
Bond: What must I do next?  > Bond moved forward by 5 steps.
 > Bond now at position (0,5).
Bond: What must I do next? Bond: Shutting down..\n""")


    @patch("sys.stdin", StringIO("hel\nforward 20\noff"))
    def test_y_coodinate(self):
        robot.robot_start()
        y_value = robot.y
        self.assertEqual(y_value, 20)


    @patch("sys.stdin", StringIO("hel\nright\nforward 15\noff"))
    def test_x_coodinate_and_right(self):
        robot.robot_start()
        x_value = robot.x
        self.assertEqual(x_value, 15)


    @patch("sys.stdin", StringIO("hel\nleft\nforward 10\noff"))
    def test_x_coodinate_and_left(self):
        robot.robot_start()
        x_value = robot.x
        self.assertEqual(x_value, -10)
    

    @patch("sys.stdin", StringIO("Bond\nback 5\noff"))
    def test_back_command(self):
        with patch("sys.stdout", new = StringIO()) as the_output:
            robot.robot_start()
            self.assertEqual(the_output.getvalue(),"""What do you want to name your robot? Bond: Hello kiddo!
Bond: What must I do next?  > Bond moved back by 5 steps.
 > Bond now at position (0,-5).
Bond: What must I do next? Bond: Shutting down..\n""")



    @patch("sys.stdin", StringIO("Magesh\nforward 201\noff"))
    def test_forward_limit(self):
        with patch("sys.stdout", new = StringIO()) as the_output:
            robot.robot_start()
            self.assertEqual(the_output.getvalue(),"""What do you want to name your robot? Magesh: Hello kiddo!
Magesh: What must I do next? Magesh: Sorry, I cannot go outside my safe zone.
 > Magesh now at position (0,0).
Magesh: What must I do next? Magesh: Shutting down..\n""")


    @patch("sys.stdin", StringIO("Magesh\nback 101\noff"))
    def test_back_limit(self):
        with patch("sys.stdout", new = StringIO()) as the_output:
            robot.robot_start()
            self.assertEqual(the_output.getvalue(),"""What do you want to name your robot? Magesh: Hello kiddo!
Magesh: What must I do next? Magesh: Sorry, I cannot go outside my safe zone.
 > Magesh now at position (0,0).
Magesh: What must I do next? Magesh: Shutting down..\n""")


    @patch("sys.stdin", StringIO("Bond\nsprint 5\noff"))
    def test_sprint_command(self):
        with patch("sys.stdout", new = StringIO()) as the_output:
            robot.robot_start()
            self.assertEqual(the_output.getvalue(),"""What do you want to name your robot? Bond: Hello kiddo!
Bond: What must I do next?  > Bond moved forward by 5 steps.
 > Bond moved forward by 4 steps.
 > Bond moved forward by 3 steps.
 > Bond moved forward by 2 steps.
 > Bond moved forward by 1 steps.
 > Bond now at position (0,15).
Bond: What must I do next? Bond: Shutting down..\n""")


if __name__ == "__main__":
    unittest.main()
