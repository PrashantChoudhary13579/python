import mesa
import seaborn as sns
import numpy as np
import pandas as pd

# class MoneyAgent(mesa.Agent):
#     def __init__(self,model):
#         super().__init__(model)
#         self.wealth = 2
#     def say_hi(self):
#         print(f"Hi! I'm an agent!{str(self.unique_id)}")

# class MoneyModel(mesa.Model):
#     def __init__(self,n , seed = None):
#         super().__init__(seed = seed)
#         self.num_agents = n
#         MoneyAgent.create_agents(model = self,n = n)
#     def step(self):
#         self.agents.shuffle_do('say_hi')
class MoneyAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, model):
        # Pass the parameters to the parent class.
        super().__init__(model)

        # Create the agent's variable and set the initial values.
        self.wealth = 1

    def exchange(self):
        # Verify agent has some wealth
        if self.wealth > 0:
            other_agent = self.random.choice(self.model.agents)
            if other_agent is not None:
                other_agent.wealth += 1
                self.wealth -= 1


class MoneyModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, n):
        super().__init__()
        self.num_agents = n

        # Create agents
        MoneyAgent.create_agents(model=self, n=n)

    def step(self):
        """Advance the model by one step."""

        # This function psuedo-randomly reorders the list of agent objects and
        # then iterates through calling the function passed in as the parameter
        self.agents.shuffle_do("exchange")