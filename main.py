from battle.envs import GridBattle
from battle.util import createN, create1v1
from battle.agents import Agent, AgentFunction, RandomAgent


@AgentFunction
def myAgent(obs, action_space, obs_space):
    return action_space.sample()


initial_map = create1v1(10)

agent1 = myAgent()

env = GridBattle((agent1, agent1), initial_map)

env.run_game(100)
