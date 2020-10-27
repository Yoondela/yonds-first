"""
TODO: You can either work from this skeleton, or you can build on your solution for Toy Robot 2 exercise.
"""

# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint',\
"print","replay", "replay silent"] #remove print
# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0
# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100
#list to keep command history
log = []
replay_count = 0
replay_commands = ["replay", "replay silent", "replay reversed", "replay reversed silent"]
on_silent = False
on_reverse = False
on_reverse_silent = False
on_replay_range = False
replay_range_helper_on = False
on_silent_range = False
on_reverse_range = False


def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """
    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)
    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """
    if len(command.split()) == 3 and is_int(command.split()[1]):
        return True
    if len(command.lower().split()) == 3:
        if "replay silent" in command.lower() and is_int(command.split()[2]):
            return True
    if "-" in command and len(command) == 10:
        x = command.split()[1].split("-")
        if is_int(x[0]) and is_int(x[1]):
            return True
    if command.lower() in replay_commands:
        return True
    else:
        (command_name, arg1) = split_command_input(command)

        return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1))
        


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
"""
def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')
def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y
def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """
    global position_x, position_y
    new_x = position_x
    new_y = position_y
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
    return False
def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
   
    if on_silent or on_reverse_silent:
        update_position(steps)
        return True
    
    else:
        if update_position(steps):
            return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
        else:
            return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'
def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if on_silent or on_reverse_silent:
        update_position(-steps)
        return True
    else:
        if update_position(-steps):
            return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
        else:
            return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'
def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index
    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0
    if on_silent or on_reverse_silent or on_replay_range:
        return True
    else:
        return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index
    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3
    if on_silent or on_reverse_silent or on_replay_range:
        return True
    else:
        return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """
    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)
def replay_range_helper(command):
    global replay_range_helper_on, on_replay_range
    x = command.split()
    a = x[1].split("-")
    if valid_range(a):
        n = a[0]
        m = a[1]
        replay_range_helper_on = False
        on_replay_range = False
        return n,m

def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """
    global on_silent, replay_range_helper_on

    do_next = True
    if command in replay_commands or on_replay_range or\
    (on_silent_range and replay_range_helper_on) or on_reverse_range:
 
        if command == "replay":
            replay(robot_name, "", "")
            show_replayed(robot_name)
            show_position(robot_name)
        
        elif "-" in command or on_replay_range and replay_range_helper_on:           
            (n,m) = replay_range_helper(command)
            replay(robot_name, n, m)
            show_replayed(robot_name)
            show_position(robot_name)
        
        elif on_silent and command == "replay silent":            
            (do_next, command_output) = replay_silent(robot_name, "")
            show_position(robot_name)
        
        elif on_reverse and "replay reversed" in command:
            if on_reverse_range:
                n = int(command.split()[2])
                replay_reversed(robot_name, n)
                show_position(robot_name)
            else:
                replay_reversed(robot_name, "")
                show_position(robot_name)

        elif on_reverse_silent and command == "replay reversed silent":
            replay_reversed_silent(robot_name)
            show_position(robot_name)

        elif on_silent_range and replay_range_helper_on:
            n = int(command.split()[2])
            replay_range_helper_on = False
            replay_silent(robot_name, n)

    else:
        (command_name, arg) = split_command_input(command)
        if command_name == 'off':
            return False
        elif command_name == 'help':
            (do_next, command_output) = do_help()
            print(command_output)
            show_position(robot_name)
        elif command_name == 'forward':
            if on_silent or on_reverse_silent:
                do_next = do_forward(robot_name, int(arg))
            else:
                (do_next, command_output) = do_forward(robot_name, int(arg))
                print(command_output)
                show_position(robot_name)
        elif command_name == 'back':
            if on_silent or on_reverse_silent:
                do_next = do_back(robot_name, int(arg))
            else:    
                (do_next, command_output) = do_back(robot_name, int(arg))
                print(command_output)
                show_position(robot_name)
        elif command_name == 'right':
            if on_silent or on_reverse_silent or on_replay_range:
                do_next = do_right_turn(robot_name)
            else:
                (do_next, command_output) = do_right_turn(robot_name)
                print(command_output)
                show_position(robot_name)
        elif command_name == 'left':
            if on_silent or on_reverse_silent or on_replay_range:
                do_next = do_left_turn(robot_name)
            else:
                (do_next, command_output) = do_left_turn(robot_name)
                print(command_output)
                show_position(robot_name)
        elif command_name == 'sprint':
            (do_next, command_output) = do_sprint(robot_name, int(arg))
            print(command_output)
            show_position(robot_name)
    return do_next


def make_history(command):
    global replay_count
    replay_list = ["forward", "back", "left", "right", "sprint"]
    if command.split()[0].lower() in replay_list:
        log.append(command)
        replay_count = replay_count + 1


def replay(robot_name, n, m):
    global current_direction_index, replay_count
    i = 0
    if is_int(m):
        x = log[int(m)-1:int(n)-1]
        replay_count = len(x)
        while i <= len(x)-1:
            handle_command(robot_name, x.pop(0))            

    elif is_int(n) and m == "":
        y = len(log) - int(n)
        replay_count = int(n)
        x = log[y:]
        while i <= len(x)-1:
            handle_command(robot_name, x.pop(0))
        show_replayed(robot_name)
        show_position(robot_name)

    elif n == "":
        current_direction_index = 0
        while i <= len(log)-1:
            handle_command(robot_name, log[i])
            i = i + 1

def show_replayed(robot_name):
    if on_replay_range:
        print(" > {} replayed {} commands silently.".format(robot_name, replay_count))
    elif on_silent:
        print(" > {} replayed {} commands silently.".format(robot_name, replay_count))
    elif on_reverse or on_reverse_range:
        print(" > {} replayed {} commands in reverse.".format(robot_name, replay_count))
    elif on_reverse_silent:
        print(" > {} replayed {} commands in reverse silently.".format(robot_name, replay_count))
    else:        
        print(" > {} replayed {} commands.".format(robot_name, replay_count))

def replay_silent(robot_name,n):
    global current_direction_index, on_silent_range, on_silent, replay_count

    i = 0
    if on_silent_range:
        y = len(log) - int(n)
        replay_count = int(n)
        x = log[y:]
        replay_count = len(x)
        on_silent = True
        while 0 <= len(x)-1:
            handle_command(robot_name, x.pop(0))
        show_replayed(robot_name)
        show_position(robot_name)
    else:
        current_direction_index = 0
        while i <= len(log)-1:
            command = log.pop(0)
            handle_command(robot_name, command)
        return True, show_replayed(robot_name)


def replay_reversed(robot_name, n):
    global current_direction_index, replay_count
    global on_reverse_range, on_reverse
    current_direction_index = 0
    i = 0
    if on_reverse_range:
        on_reverse_range = False
        y = int(n)
        x = log[:y]
        replay_count = len(x)
        while i <= len(x)-1:
            z = len(x)-1
            command = x.pop(z)
            handle_command(robot_name, command)
        return True, show_replayed(robot_name)
    elif n == "":    
        while i <= len(log)-1:
            x = len(log)-1
            command = log.pop(x)
            handle_command(robot_name, command)
        return True, show_replayed(robot_name)

def valid_range(int_lst):
    if int(int_lst[0]) > int(int_lst[1]):
        return True
    else:
        print("first number must be bigger than the second number in range\
 eg 'replay 5-2'")
        return True

def replay_reversed_silent(robot_name):
    global current_direction_index
    current_direction_index = 0
    i = 0
    while i <= len(log)-1:
        command = log.pop(0)
        handle_command(robot_name, command)
    return True, show_replayed(robot_name)

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def rearange_command(command):
    x = command.split()
    new_x = []
    new_x.append(x[0])
    new_x.append(x[2])
    new_x.append(x[1])
    new_command = " ".join(new_x)
    return new_command

def robot_start():
    """This is the entry point for starting my robot"""
    global position_x, position_y, current_direction_index, on_silent
    global on_reverse, on_reverse_silent, on_replay_range, on_reverse_range
    global replay_range_helper_on, on_silent_range,log, replay_count
    log = []
    replay_count = 0
    position_x = 0
    position_y = 0
    current_direction_index = 0
    on_silent = False
    on_reverse = False
    on_reverse_silent = False
    on_replay_range = False
    replay_range_helper_on = False
    on_silent_range = False
    on_reverse_range = False

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

   
    command = get_command(robot_name)

    if command.lower() == "replay silent":
        on_silent = True
    elif command.lower() == "replay reversed":
        on_reverse = True
    elif command.lower() == "replay reversed silent":
        on_reverse_silent = True
    
    make_history(command)
    while handle_command(robot_name, command):
        command = get_command(robot_name)
        make_history(command)
        if len(command.split()) == 3 and is_int(command.split()[1]):
            if command.split()[2] == "reversed":
                on_reverse_range = True
                on_reverse = True
            command = rearange_command(command)
        if len(command.split()) == 2:
            if command.lower() == "replay silent":
                on_silent = True
            elif command.lower() == "replay reversed":
                on_reverse = True

            elif command.lower().split()[0] == "replay" and is_int(command.split()[1]):
                replay(robot_name, command.split()[1], "")           
            elif "-" in command:
                on_replay_range = True
                replay_range_helper_on = True

        if len(command.split()) == 3:
            if command.lower() == "replay reversed silent":
                on_reverse_silent = True
            if "replay silent" in command.lower() and is_int(command.split()[2]):
                on_silent_range = True
                replay_range_helper_on = True

        
        
    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()
"""
left at: reversed silent
"""
