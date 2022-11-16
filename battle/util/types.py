from enum import IntEnum


# in the main environment, this is stored with an np.byte, so it can only go up to 127 (126 agents max)
class Tiles(IntEnum):
    EMPTY = 0  # unclaimed, no bot or wall on this tile
    WALL = 1  # tile with a wall on it
    AGENT = 2  # local agents (each agents sees its own territory in this layer)
    # 3, 4, 5... are the ids of the other agents

    def __getattr__(self, attr: str) -> int:
        if not attr.startswith('AGENT_'):
            raise AttributeError()

        attr_tokens = attr.split('_')
        if len(attr_tokens) != 2:
            raise AttributeError('Please use Tiles.AGENT_N, where N is an integer')

        rel_agent_id = attr_tokens[1]
        if not rel_agent_id.isdigit():
            raise AttributeError('Please use Tiles.AGENT_N, where N is an integer')

        agent_id = int(rel_agent_id) + self.AGENT

        return agent_id
