import enum
from tokenize import String

# The size of the table
tableX = 5
tableY = 5


class Direction(enum.Enum):
    '''The four directions as both strings and ints'''
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    # This method came from https://stackoverflow.com/a/66891151
    @classmethod
    def hasMemberKey(cls, key):
        '''Check if the passed in direction is a valid direction'''
        return key in cls.__members__


class Robot:
    x: int
    y: int
    dir: Direction

    def place(self, x: int, y: int, dir: str) -> bool:
        '''Place the robot on the table'''

        if x < 0 or tableX <= x:
            print(f"Failed to place robot, x of {x} is off the table")
            return False
        elif y < 0 or tableY <= y:
            print(f"Failed to place robot, y of {y} is off the table")
            return False
        elif not Direction.hasMemberKey(dir):
            print(f"Failed to place robot, {dir} is not a valid direction")
            return False
        else:
            self.x = x
            self.y = y
            self.dir = Direction[dir]
            return True

    def rotate(self, dir: str):
        '''Rotate the robot either left or right, signified by R and L'''

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
        '''Move the robot forward one space in the direction it is facing,
        making sure it doesn't fall off the table'''

        if self.dir == Direction.NORTH:
            if self.y != tableY - 1:
                self.y += 1
        if self.dir == Direction.EAST:
            if self.x != tableX - 1:
                self.x += 1
        if self.dir == Direction.SOUTH:
            if self.y != 0:
                self.y -= 1
        if self.dir == Direction.WEST:
            if self.x != 0:
                self.x -= 1

    def report(self):
        '''Output the robot's position and the direction it is facing'''

        print(f"Robot is at {self.x}, {self.y}, facing {self.dir.name}")
