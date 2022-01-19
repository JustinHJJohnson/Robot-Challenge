from io import TextIOWrapper
import Robot


def main():

    robots: list[Robot.Robot] = []  # A list of all the active robots
    activeRobot: int = ()           # The index of the current active robot
    debug = False                   # Enables debug print statements

    # Open and read in the input file
    input = open('Tests/bigTest.txt', 'r')
    lines = input.readlines()

    # Loop over every instruction in the input file
    for line in lines:

        instruction: str = line.split()

        if debug:
            print(instruction)

        # Check if the place command has been run yet, if not check if the
        # current command is place
        if len(robots) == 0 and instruction[0] != "PLACE":
            continue

        # Parse the current instruction
        if instruction[0] == "PLACE":
            values = instruction[1].split(',')
            if debug:
                print(
                    (
                        f'Ran place with {int(values[0])} {int(values[1])}'
                        f' {values[2]}'
                    )
                )
            robo = Robot.Robot()
            if robo.place(int(values[0]), int(values[1]), values[2]):
                robots.append(robo)
                activeRobot = len(robots) - 1
        elif instruction[0] == "MOVE":
            if debug:
                print("Ran move")
            robots[activeRobot].move()
        elif instruction[0] == "LEFT":
            if debug:
                print("Ran left")
            robots[activeRobot].rotate('L')
        elif instruction[0] == "RIGHT":
            if debug:
                print("Ran right")
            robots[activeRobot].rotate('R')
        elif instruction[0] == "REPORT":
            if debug:
                print("Ran report")
            robots[activeRobot].report()
        elif instruction[0] == "ROBOT":
            inputIndex = int(instruction[1]) - 1
            if inputIndex >= len(robots):
                print(
                    (
                        f"Failed to switch robots, {inputIndex + 1} is not a"
                        " valid robot"
                    )
                )
            else:
                activeRobot = inputIndex
        else:
            print(f"The command {line.strip()} is not valid")

if __name__ == "__main__":
    main()
