obs = [(34,78), (7,90), (1,9)]

x_change = False
ocupied = []


def is_position_blocked(x,y):
    pos =(x,y)
    for i in range(3):
        obstacle = obs[i]
        helper(obstacle)
    if pos in ocupied:
        return True
    else:
        return False

def is_blocked():
    for i in range(3):
        obstacle = obs[i]
        helper(obstacle)


def helper(obstacle):
    global ocupied, x_change
    (x,y) = obstacle
    y_marker = y
  
    for i in range(6):
        for j in range(5):
            ocupied.append((x,y))              
            
            if x_change:
                y = y_marker
                ocupied.append((x,y))
                x_change = False
            y = y + 1
        x = x - 1
        x_change = True


def is_path_blocked(x1,y1,x2,y2):
    start = (x1,y1)
    end = (x2, y2)
    start_x = start[0]
    end_x = end[0]
    start_y = start[1]
    end_y = end[1]
    blocked = False
    if start_x <= end_x:
        for i in range(start_x, end_x+1):
            if start_y <= end_y:
                for j in range(start_y, end_y):
                    if start_y < end_y:
                        start_y = start_y + 1
                    else:
                        start_y = start_y - 1
                    if (start_x,start_y) in ocupied:
                        blocked = True

            elif start_y > end_y:
                for j in range(end_y, start_y):
                    if start_y < end_y:
                        start_y = start_y + 1
                    else:
                        start_y = start_y - 1
                    if (start_x,start_y) in ocupied:
                        blocked = True

            if start_x < end_x:
                start_x = start_x + 1
            elif start_x > end_x:
                start_x = start_x - 1

    elif start_x > end_x:
        for i in range(end_x, start_x+1):
            if start_y <= end_y:
                for j in range(start_y, end_y):
                    if start_y < end_y:
                        start_y = start_y + 1
                    else:
                        start_y = start_y - 1
                    if (start_x,start_y) in ocupied:
                        blocked = True

            elif start_y > end_y:
                for j in range(end_y, start_y):
                    if start_y < end_y:
                        start_y = start_y + 1
                    else:
                        start_y = start_y - 1
                    if (start_x,start_y) in ocupied:
                        blocked = True

            if start_x < end_x:
                start_x = start_x + 1
            elif start_x > end_x:
                start_x = start_x - 1
    return blocked



print(is_position_blocked(32,78))
print(is_path_blocked(-3,-12,3,-45))

