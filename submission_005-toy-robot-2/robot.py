
def name_the_robot():
    name_of_robot = input("What do you want to name your robot? ")
    print(name_of_robot + ": Hello kiddo!")
    return name_of_robot


def get_command_input(name):
    user_input = input(f"{name}: What must I do next? ")
    new_input = user_input.casefold()
    return new_input, user_input


def moving_forward(input_from_user,name, direction, x, y):
    old_y = y
    old_x = x
    valid = False
    instruction = input_from_user.split()[0]
    steps = int(input_from_user.split()[1])
    same = (instruction, steps) 
    if direction == 1:
        new_y = old_y + int(steps)
        if new_y in range(-200,200):
            print(" > {} moved forward by {} steps.".format(name, steps))
            y = new_y
            valid = True
    elif direction == 0 or direction == 4:
        new_x = old_x - int(steps)
        if new_x in range(-100,100):
            print(" > {} moved forward by {} steps.".format(name, steps))
            x = new_x
            valid = True
    elif direction == 2 or direction == -2:
        new_x = old_x + int(steps)
        if new_x in range(-100,100):
            print(" > {} moved forward by {} steps.".format(name, steps))
            x = new_x
            valid = True
    elif direction == -1 or direction == 3:
        new_y = old_y - int(steps)
        if new_y in range(-200,200):
            print(" > {} moved forward by {} steps.".format(name, steps))
            y = new_y
            valid = True
    return x, y, direction, instruction, valid, steps


def moving_backward(input_from_user, name, direction, x, y):
    old_y = y
    old_x = x
    valid = False
    instruction = input_from_user.split()[0]
    steps = int(input_from_user.split()[1])
    same = (instruction, steps)
    if direction == 1:
        new_y = old_y - int(steps)
        if new_y in range (-200, 200):
            print(" > {} moved back by {} steps.".format(name, steps))
            y = new_y
            valid = True
    elif direction == 0 or direction == 4:
        new_x = old_x + int(steps)
        if new_x in range(-100,100):
            print(" > {} moved back by {} steps.".format(name, steps))
            x = new_x
            valid = True
    elif direction == 2 or direction == -2:
        new_x = old_x - int(steps)
        if new_x in range(-100,100):
            print(" > {} moved back by {} steps.".format(name, steps))
            x = new_x
            valid = True
    elif direction == -1 or direction == 3:
        new_y = old_y + int(steps)
        if new_y in range (-200,200):
            print(" > {} moved back by {} steps".format(name, steps))
            y = new_y
            valid = True
    return x, y, direction, instruction, valid, steps


def keep_track_of_position(x, y, steps, name, direction, valid):
    if valid:
        print(" > {} now at position ({},{}).".format(name,x, y)) 
    else:
        print("{}: Sorry, I cannot go outside my safe zone.".format(name))
        print(f" > {name} now at position ({x},{y}).")
    return x, y, direction


def keep_track_of_sprint(input_from_user,x, y, name, direction, steps):
    if steps > 0:
        input_from_user = f"sprint {steps}"
        x, y, direction, instruction, valid, steps = moving_forward(input_from_user, name, direction, x, y)
        steps = steps - 1
        return keep_track_of_sprint(input_from_user, x, y, name, direction, steps)
    else:
        return x,y


def direction_left(direction, name, x, y):
    if direction == 'n':
        direction = "w"
    if direction == 'w':
        direction = "s"
    if direction == 's':
        direction = "e"
    direction = direction - 1
    if direction < -2:
        direction = 1
    print(f" > {name} turned left.")
    print(" > {} now at position ({},{}).".format(name, x, y))
    return direction


def direction_right(direction, name, x, y):
    direction = direction + 1
    if direction > 4:
        direction = 1
    print(f" > {name} turned right.")
    print(" > {} now at position ({},{}).".format(name, x, y))
    return direction


def need_help():
    print("I can understand these commands:")
    print("OFF  - Shut down robot")
    print("HELP - provide information about commands")
    print(" FORWARD - in the direction that one is facing or travelling")
    print(" BACK - in the direction that one is not facing or travelling")
    print(" SPRINT - accelerates in the direction that one is not facing or travelling")
    print(" LEFT - turns left")
    print(" RIGHT - turns right")


def off_command(name):
    print(f"{name}: Shutting down..")
    return False


def invalid_command(user_input, name):
    print(f"{name}: Sorry, I did not understand '{user_input}'.")
    robot_start


def robot_start():
    x = 0
    y = 0
    old_x = 0
    old_y = 0
    direction = 1
    steps = 0
    commands = ["off", "help", "forward", "back", "right", "up", "left", "down", "sprint"]
    robot_on = True
    valid = False
    name = name_the_robot()
    while robot_on:
        input_from_user, new_input = get_command_input(name)
        cmd = input_from_user.split(" ")

        if "help" in input_from_user:
            need_help()

        elif "off" in input_from_user:
            robot_on = off_command(name)

        elif "forward" == cmd[0] and cmd[1].isdigit():
            x, y, direction, instruction, valid, steps = moving_forward(input_from_user, name, direction, x, y )
            x, y, direction = keep_track_of_position(x, y, int(cmd[1]), name, direction, valid)

        elif "back" == cmd[0] and cmd[1].isdigit():
            x, y , direction, instruction, valid, steps = moving_backward(input_from_user, name, direction, x, y )
            x, y, direction = keep_track_of_position(x, y, int(cmd[1]), name, direction, valid)

        elif input_from_user == "left":
            direction = direction_left(direction, name, x, y)

        elif input_from_user == "right":
            direction = direction_right(direction, name, x, y)

        elif "sprint" in cmd and cmd[1].isdigit():
            x, y = keep_track_of_sprint(input_from_user,x, y, name, direction, int(cmd[1]))
            print(" > {} now at position ({},{}).".format(name,x, y))

        else:
            invalid_command(new_input, name)


if __name__ == "__main__":
    robot_start()
