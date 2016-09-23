# -*- coding: UTF-8 -*-

#----Built-in packages----#
from random import uniform

#----Installed packages----#
from mesa import Model
from mesa.time import RandomActivation
from mesa.space import ContinuousSpace

#----Import Classes----#
from person import Person
from zombie import Zombie


class Zombieland(Model):
    """docstring for Zombieland."""
    def __init__(self, n_persons=30, n_zombies=10, allowed_area=(10.0, 10.0),
            time_step=1, max_speed_person=1, max_speed_zombie=0.5):
        self.n_persons = n_persons
        self.n_zombies = n_zombies
        self.time_step = time_step
        self.max_speed_person = max_speed_person
        self.max_speed_zombie = max_speed_zombie

        self.schedule = RandomActivation(self)
        self.grid = ContinuousSpace(x_max = allowed_area[0],
                y_max = allowed_area[1], torus = False)
        #Create persons
        for i in range(self.n_persons):
            speed = uniform(0.0, self.max_speed_person)
            unique_id = i
            p = Person(unique_id, self, speed)
            self.schedule.add(p)

            # Add the agent to a random grid cell
            x = uniform(0.0, self.grid.x_max)
            y = uniform(0.0, self.grid.y_max)
            self.grid.place_agent(p, (x, y))

        for j in range(self.n_zombies):
            speed = uniform(0.0, self.max_speed_zombie)
            unique_id = j+i
            z = Zombie(unique_id, self, speed)
            self.schedule.add(z)

            # Add the agent to a random grid cell
            x = uniform(0.0, self.grid.x_max)
            y = uniform(0.0, self.grid.y_max)
            self.grid.place_agent(z, (x, y))

    def get_num_agents(self, agent_type="Person"):
        cont = 0
        for a in self.schedule.agents:
            if a.__class__.__name__ == agent_type:
                cont += 1
        return cont

    def step(self):
        '''Advance the model by one step.'''
        print("New iteration")
        self.schedule.step()
        persons = self.get_num_agents("Person")
        zombies = self.get_num_agents("Zombie")
        print("Persons:", persons)
        print("Zombies:", zombies)
        print("")
        return persons

def main():
    model = Zombieland()
    for i in range(1000):
        if model.step() == 0:
            break

if __name__ == '__main__':
    main()
