import enum

tableX = 5
tableY = 5

class Direction(enum.Enum):
    North = 0
    East = 1
    South = 2
    West = 3

class Robot:
    x = None
    y = None
    dir = None

    def place(self, x, y, dir):
        '''Place a robot on the table and return it'''
        if 0 < x < tableX - 1: 
            x = x
        if 0 < y < tableY - 1: 
            y = y
        dir = dir
    
    def rotate(self, dir):
        '''Rotate the given robot either left or right, signified by R and L'''
        if dir == 'R':
            newDir = Direction((self.dir.value + 1) % 4)
            self.dir = newDir
        if dir == 'L':
            newDir = Direction((self.dir.value - 1) % 4)
            self.dir = newDir

    def move(self):
        '''Move the robot forward one space in the direction it is facing, making sure it doesn't fall off the table'''
        if self.dir == Direction.North:
            if self.x != tableX - 1:
                self.x += 1
        if self.dir == Direction.East:
            if self.y != tableY - 1:
                self.y += 1
        if self.dir == Direction.South:
            if self.x != 0:
                self.x -= 1
        if self.dir == Direction.West:
            if self.y != 0:
                self.y -= 1

    def report(self):
        '''Output the provided robot's number, current position and the direction it is facing'''
        print(f"Robot is at {self.x} {self.y}, facing {self.dir.name}")

            
