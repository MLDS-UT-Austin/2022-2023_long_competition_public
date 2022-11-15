import numpy as np
import math
from typing import Tuple
from numpy.typing import NDArray
from .types import Tiles
from functools import partial

# Util functions for creating maps


def createEmpty(shape: Tuple[int, int] | int) -> NDArray[int]:
    """
    Creates an empty map of specified shape

    :param shape: Either the height/width of the grid or the side length
    :type shape: Tuple[int, int] | int
    :return: An empty map of the given size
    :rtype: NDArray
    """
    if isinstance(shape, int):
        shape = (shape, shape)

    return np.full(shape, Tiles.EMPTY, dtype=np.ubyte)


def createN(shape: Tuple[int, int] | int, num_agents: int) -> NDArray[int]:
    """
    Creates a map of specified shape that is empty except for starting positions for N agents

    :param shape: Either the height/width of the grid or the side length
    :type shape: Tuple[int, int] | int
    :param num_agents: The number of agents to start with
    :type num_agents: int
    :return: A n-agent battle royale map of the given size
    :rtype: NDArray
    """
    if isinstance(shape, int):
        shape = (shape, shape)

    new_map = createEmpty(shape)

    agents_per_side = 1 + math.isqrt(num_agents - 1)
    max_possible_agents = agents_per_side ** 2

    for i in range(num_agents):
        if i % 2 == 0:
            i_pos = i // 2
        else:
            i_pos = max_possible_agents - ((i + 1) // 2)
        agent_id = i + Tiles.AGENT
        agent_axis_0 = ((i_pos // agents_per_side) * shape[0]) // agents_per_side
        agent_axis_1 = ((i_pos % agents_per_side) * shape[1]) // agents_per_side

        new_map[agent_axis_0, agent_axis_1] = agent_id


    return new_map


# Creates a map of specified shape that is empty except for two cells to 1v1
create1v1 = partial(createN, num_agents=2)
