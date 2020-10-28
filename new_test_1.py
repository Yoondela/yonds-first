import unittest
import robot
from unittest.mock import patch
from io import StringIO
import sys


class test_toy(unittest.TestCase):
    @patch("sys.stdin", StringIO("hel\nplay\noff\n"))
    def test_valid_input(self):
        with patch("sys.stdout", new = StringIO()) as the_output:
            robot.robot_start()
            self.assertEqual(the_output.getvalue().strip(),"""What do you want to name your robot? hel: Hello kiddo!
hel: What must I do next? hel: Sorry, I did not understand 'play'.
hel: What must I do next? hel: Shutting down..""")

    @patch("sys.stdin", StringIO("Rob\nhelp\noff\n"))
    def test_help_command(self):
        self.maxDiff = None
        value = robot.do_help()
        self.assertEqual(value,(True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays the commands you have used
REPLAY SILENT - replays the commands you have used silently
REPLAY REVERSE - replays the commands you have used in reverse
REPLAY N - replays the last number of commands eg replay 2
REPLAY N-M - replays used commands in range of n and m eg replay 4-2
REPLAY SILENT N - replays the last number of commands silently eg replay 2
REPLAY REVERSED N - replays the last number of commands in reverse eg replay 2
"""))


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
        y_value = robot.position_y
        self.assertEqual(y_value, 20)


    @patch("sys.stdin", StringIO("hel\nright\nforward 15\noff"))
    def test_x_coodinate_and_right(self):
        robot.robot_start()
        x_value = robot.position_x
        self.assertEqual(x_value, 15)


    @patch("sys.stdin", StringIO("hel\nleft\nforward 10\noff"))
    def test_x_coodinate_and_left(self):
        robot.robot_start()
        x_value = robot.position_x
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


    @patch("sys.stdin", StringIO("Magesh\nback 201\noff"))
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
