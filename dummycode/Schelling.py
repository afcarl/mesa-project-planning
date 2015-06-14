'''
Python ABM Dummy Code
====================================

Schelling Segregation Model
'''

from __future__ import division # We're doing this in Python 2.x, right?
import random

from mesa import Model, Agent
from mesa.time import Random_Activation
from mesa.space import AgentGrid

class SchellingModel(Model):
    '''
    Model class for the Schelling segregation model.
    '''

    def __init__(self, height, width, density, minority_pc, homophily):
        '''
        '''

        self.height = height
        self.width = width
        self.density = density
        self.minority_pc = minority_pc
        self.homophily = homophily

        self.schedule = Random_Activation(self)
        self.grid = AgentGrid(height, width)

        self.happy_series = []
        self.happy = 0

        # Set up agents
        for x in range(self.width):
            for y in range(self.height):
                if random.random() < self.density:
                    if random.random() < self.minority_pc:
                        agent_type = 1
                    else:
                        agent_type = 0
                    agent = SchellingAgent(x, y, agent_type)
                    grid[y][x] = agent
                    self.schedule.add(agent)

    def get_empty(self):
        empty_cells = []
        for x in range(self.width):
            for y in range(self.height):
                if grid[y][x] is None:
                    empty_cells.append((x, y))
        return empty_cells

    def go(self):
        self.happy = 0 # Reset counter of happy agents
        self.schedule.step()
        self.happy_series.append(happy)


class SchellingAgent(Agent):Age
    '''
    Schelling segregation agent
    '''
    def __init__(self, x, y, agent_type):
        self.x = x
        self.y = y
        self.type = agent_type

    def step(self, model):
        neighbors = model.grid.get_neighbors(self.x, self.y, moore=True)
        similar = 0
        for neighbor in neighbors:
            if neighbor.type == self.type:
                similar += 1

        # If unhappy, move:
        if similar < model.homophily:
            new_x, new_y = random.choice(mode.get_empty())
            grid[self.y][self.x] = None
            grid[new_y][new_x] = self
        else:
            model.happy += 1


if __name__ == "__main__":
    model = Model(10, 10, 0.8, 0.2, 3)
    while model.happy < model.model.schedule.get_agent_count():
        model.go()





