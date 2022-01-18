import enum

# The size of the table
tableX = 5
tableY = 5

class Direction(enum.Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Robot:
    x = None
    y = None
    dir = None

    def place(self, x, y, dir):
        '''Place a robot on the table and return it'''
        if 0 <= x <= tableX - 1: 
            self.x = x
        else:
            print(f"Failed to place robot, {x} is off the table")
        if 0 <= y <= tableY - 1: 
            self.y = y
        else:
            print(f"Failed to place robot, {y} is off the table")
        self.dir = Direction[dir]
    
    def rotate(self, dir):
        '''Rotate the given robot either left or right, signified by R
        and L'''
        if dir == 'R':
            newDir = Direction((self.dir.value + 1) % 4)
            self.dir = newDir
        elif dir == 'L':
            newDir = Direction((self.dir.value - 1) % 4)
            self.dir = newDir
        else:
            print(
                """Failed to rotate, {dir} is not a valid direction to
                rotate. (Please use L or R)"""
            )

    def move(self):
        '''Move the robot forward one space in the direction it is 
        facing, making sure it doesn't fall off the table'''
        if self.dir == Direction.NORTH:
            if self.x != tableX - 1:
                self.x += 1
        if self.dir == Direction.EAST:
            if self.y != tableY - 1:
                self.y += 1
        if self.dir == Direction.SOUTH:
            if self.x != 0:
                self.x -= 1
        if self.dir == Direction.WEST:
            if self.y != 0:
                self.y -= 1

    def report(self):
        '''Output the provided robot's number, current position and the
        direction it is facing'''
        print(f"Robot is at {self.x} {self.y}, facing {self.dir.name}")

            
