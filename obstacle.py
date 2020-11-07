obs = [(34,78), (7,90), (1,9)]

y_change = False
ocupied = []
def is_position_blocked(y,x):
    pos =(y,x)
    for i in range(3):
        obstacle = obs[i]
        helper(obstacle)
    if pos in ocupied:
        return True
    else:
        return False

def is_path_blocked(start, end):
    # start = [16,6]
    # end = [103,8]
    start_y = start[0]
    end_y = end[0]
    start_x = start[1]
    end_x = end[1]
    if start_y <= end_y:
        for i in range(start_y, end_y+1):
            if start_x <= end_x:
                for j in range(start_x, end_x):
                    if start_x < end_x:
                        start_x = start_x + 1
                    else:
                        start_x = start_x - 1
                    if (start_y,start_x) in ocupied:
                        print("thers an obstacle in the path")
                    print("{},{}".format(start_y, start_x))

            elif start_x > end_x:
                for j in range(end_x, start_x):
                    if start_x < end_x:
                        start_x = start_x + 1
                    else:
                        start_x = start_x - 1
                    if (start_y,start_x) in ocupied:
                        print("thers an obstacle in the path")

                    print("{},{}".format(start_y, start_x))
            if start_y < end_y:
                start_y = start_y + 1
            elif start_y > end_y:
                start_y = start_y - 1
            print("{},{}".format(start_y, start_x))

    elif start_y > end_y:
        for i in range(end_y, start_y+1):
            if start_x <= end_x:
                for j in range(start_x, end_x):
                    if start_x < end_x:
                        start_x = start_x + 1
                    else:
                        start_x = start_x - 1
                    if (start_y,start_x) in ocupied:
                        print("thers an obstacle in the path")
                    print("{},{}".format(start_y, start_x))

            elif start_x > end_x:
                for j in range(end_x, start_x):
                    if start_x < end_x:
                        start_x = start_x + 1
                    else:
                        start_x = start_x - 1
                    if (start_y,start_x) in ocupied:
                        print("thers an obstacle in the path")

                    print("{},{}".format(start_y, start_x))
            if start_y < end_y:
                start_y = start_y + 1
            elif start_y > end_y:
                start_y = start_y - 1
            print("{},{}".format(start_y, start_x))
        

def is_blocked():
    for i in range(3):
        obstacle = obs[i]
        helper(obstacle)


def helper(obstacle):
    global ocupied, y_change
    (y,x) = obstacle
    x_marker = x
  
    for i in range(6):
        for j in range(5):
            ocupied.append((y,x))              
            
            if y_change:
                x = x_marker
                ocupied.append((y,x))
                y_change = False
            x = x + 1
        y = y - 1
        y_change = True

print(is_position_blocked(32,78))
print(ocupied)
is_path_blocked([56,12], [7,-45])

    
