import turtle
# from world.text import world as a

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100
bob = turtle.Turtle()
s = turtle.Screen()

def draw_border():
    y = turtle.Turtle()
    y.penup()
    y.pensize(4)
    y.pencolor("green")
    y.setposition(-350, -500)
    y.pendown()
    y.forward(700)
    y.left(90)
    y.forward(1200)
    y.left(90)
    y.forward(700)
    y.left(90)
    y.forward(1200)
    y.hideturtle()

draw_border()

def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')
    return robot_name


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """
    global position_x, position_y
    new_x = position_x
    new_y = position_y
    
    while True:
        if directions[current_direction_index] == 'forward':
            new_y = new_y + steps
        elif directions[current_direction_index] == 'right':
            new_x = new_x + steps
        elif directions[current_direction_index] == 'back':
            new_y = new_y - steps
        elif directions[current_direction_index] == 'left':
            new_x = new_x - steps
        if is_position_allowed(new_x, new_y):
            position_x = new_x
            position_y = new_y
            return True
        turtle.done()
        return False

def is_position_allowed(new_x, new_y):
    
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y





