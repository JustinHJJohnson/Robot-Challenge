from operator import contains
import Robot

def main():
    
    robots = []         # A list of all the active robots
    activeRobot = ()    # The index of the current active robot
    
    # Open and read in the input file
    input = open('input.txt', 'r')
    lines = input.readlines()

    # Loop over every instruction in the input file
    for line in lines:
        # Check if the place command has been run yet, if not check if
        # the current command is place
        if len(robots) == 0 and not "PLACE" in line:
            continue
        
        # Parse the current instruction
        if "PLACE" in line:
            #print(f"Ran place with {int(line[6])} {int(line[8])} {line[10:].strip()}")
            temp = Robot.Robot()
            temp.place(int(line[6]), int(line[8]), line[10:].strip())
            robots.append(temp)
            activeRobot = len(robots) - 1
        elif "MOVE" in line:
            #print("Ran move")
            robots[activeRobot].move()
        elif "LEFT" in line:
            #print("Ran left")
            robots[activeRobot].rotate('L')
        elif "RIGHT" in line:
            #print("Ran right")
            robots[activeRobot].rotate('R')
        elif "REPORT" in line:
            #print("Ran report")
            robots[activeRobot].report()
        elif "ROBOT" in line:
            activeRobot = int(line[6])
        else:
            print(f"The command {line.strip()} is not valid")

if __name__=="__main__":
    main()