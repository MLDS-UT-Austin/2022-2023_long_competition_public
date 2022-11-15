from enum import IntEnum


# in the main environment, this is stored with an np.byte, so it can only go up to 127 (126 agents max)
class Tiles(IntEnum):
    EMPTY = 0  # unclaimed, no bot or wall on this tile
    WALL = 1  # tile with a wall on it
    AGENT = 2  # local agents (each agents sees its own territory in this layer)
    # 3, 4, 5... are the ids of the other agents
