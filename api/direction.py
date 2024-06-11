from collections import namedtuple
from enum import Enum

class Direction(Enum):
    """
    An enumeration representing the possible directions in which the snake can move.
    
    Attributes:
    RIGHT (int): Represents the right direction.
    LEFT (int): Represents the left direction.
    UP (int): Represents the upward direction.
    DOWN (int): Represents the downward direction.
    """
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x y')
"""
A named tuple representing a point in a 2D space.

Attributes:
x (int): The x-coordinate of the point.
y (int): The y-coordinate of the point.
"""

# Example usage
if __name__ == "__main__":
    # Create a point
    point = Point(x=5, y=10)
    print(f"Point coordinates: x={point.x}, y={point.y}")
    
    # Create a direction
    direction = Direction.RIGHT
    print(f"Current direction: {direction.name}")
    
    # Check the direction
    if direction == Direction.RIGHT:
        print("Moving right")
