from operator import contains
import Robot

def main():
    
    robots = []
    activeRobot = ()
    numRobots = 0
    
    input = open('input.txt', 'r')
    lines = input.readlines()

    # Loop over every instruction in the input file
    for line in lines:
        # Check if the place command has been run yet, if not check if the current command is place
        if len(robots) == 0 and not "PLACE" in line:
            continue
        
        # Parse the current instruction
        if "PLACE" in line:
            print("Ran place")
            temp = Robot.Robot()
            temp.place(int(line[6]), int(line[8]), line[10])
            robots.append(temp)
            numRobots += 1
            activeRobot = numRobots
        if "MOVE" in line:
            print("Ran move")
            robots[activeRobot - 1].move()
        if "LEFT" in line:
            print("Ran left")
            robots[activeRobot - 1].rotate('L')
        if "RIGHT" in line:
            print("Ran right")
            robots[activeRobot - 1].rotate('R')
        if "REPORT" in line:
            print("Ran report")
            robots[activeRobot - 1].report()





if __name__=="__main__":
    main()