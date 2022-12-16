import random
from typing import List
#Environment class: its a model of the world which is external to the agent.it provides observations and rewards to agent
class SampleEnvirnment:
    def __init__(self):
        self.steps_left=20
    def get_observations(self):
        return[0.0,0.0,0.0]
    def get_actions(self):
        return[0,1]
    def is_done(self):
        return self.steps_left==0
    def action(self,action:int):
        if self.is_done():
            raise Exception("Game over")
        self.steps_left -=1
        return random.random()
#Agent class:A thing or person that tries to get rewards by interactions (piee of code that implement some policy)
class Agent:
    def __init__(self):
        self.total_reward=0.0
#step function accept envirnment instance
# 1:obser the environment
#2:Make decision about action based on observations
#3:submit the action to envirnment
#4:Get the reward for current step

    def step(self,env:SampleEnvirnment):
        current_obs=env.get_observations()
        print("Observation {}".format(current_obs))
        action=env.get_actions()
        print(action)
        reward=env.action(random.choice(action))
        self.total_reward+=reward
        print("Total reward{}".format(self.total_reward))

def main():
    print("---Reinforcement learning----")
    env=SampleEnvirnment()
    agent=Agent()
    i=0

    while not env.is_done():
        i+=1
        print("Step no{}".format(i))
        agent.step(env)
    print("Total reward got:%.4f" %agent.total_reward)
if __name__=="__main__":
    main()
