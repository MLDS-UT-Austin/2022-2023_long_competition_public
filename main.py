import gym
from numpy.typing import NDArray
from battle.envs import GridBattle
from battle.util import createN, create1v1
from battle.agents import Agent, AgentFunction

num_agents = 2  # Try changing this and see what happens!

initial_map = createN(10, num_agents)


@AgentFunction
def myAgent(obs: NDArray[int], action_space: gym.Space, obs_space: gym.Space) -> NDArray:
    return action_space.sample()


agent1 = myAgent()

env = GridBattle((agent1,) * num_agents, initial_map)

env.run_game(100)
