from ps2 import *

room = RectangularRoom(5, 4)
room.showRoom()
print(f"Number of tiles: {room.getNumTiles()}")
print(f"Number of clean tiles: {room.getNumCleanedTiles()}")

position = Position(0.5, 1.2)
room.cleanTileAtPosition(position)
room.showRoom()
print(f"Number of tiles: {room.getNumTiles()}")
print(f"Number of clean tiles: {room.getNumCleanedTiles()}")

position = room.getRandomPosition()
room.cleanTileAtPosition(position)
room.showRoom()
print(f"Number of tiles: {room.getNumTiles()}")
print(f"Number of clean tiles: {room.getNumCleanedTiles()}")

print(room.isPositionInRoom(position))
position = Position(0.5, 10)
print(room.isPositionInRoom(position))

robot = Robot(room, 1)
print(robot.getRobotPosition())
print(robot.getRobotDirection())
room.showRoom()
