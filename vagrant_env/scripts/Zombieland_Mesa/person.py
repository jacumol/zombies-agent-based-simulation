# -*- coding: UTF-8 -*-

#----Built-in packages----#
import math
from random import uniform

#----Installed packages----#
from mesa import Agent

#----Import Classes----#

class Person(Agent):
    """docstring for Person."""
    def __init__(self, unique_id, model, speed,
            observation_radius=50):
        super().__init__(unique_id, model)
        self.speed = speed #Speed given in m/s
        self.observation_radius = observation_radius #Given in meters

    def get_closest_zombie(self):
        """
            This function gets the direction of movement according to the
            nearest zombie
        """
        #Get all the agents in the observation radius
        neighbors = self.model.grid.get_neighbors(self.pos,
                self.observation_radius, include_center=False)

        closest_pos = None
        min_distance = 99999999999999999999
        for n in neighbors:
            #If it's a zombie, get the position and distance.
            if n.__class__.__name__ == "Zombie":
                distance = self.model.grid.get_distance(self.pos, n.pos)
                if distance <= min_distance:
                    closest_pos = n.pos

        return closest_pos

    def get_next_moving_direction(self, nearest_zombie_pos=None):
        """
            Function that computes next direction according to where
            the nearest zombie is.
        """
        if nearest_zombie_pos is None:
            nearest_zombie_pos=(uniform(0.0, self.model.grid.x_max),
                                uniform(0.0, self.model.grid.y_max))

        vector = (self.pos[0]-nearest_zombie_pos[0],
                  self.pos[1]-nearest_zombie_pos[1])

        magnitude = math.sqrt(vector[0]**2 + vector[1]**2)
        if magnitude == 0:
            magnitude = 0.0000001

        direction_vector = (vector[0]/magnitude, vector[1]/magnitude)
        return direction_vector


    def move_next_point(self):
        """
            Function that moves the agent according to his speed and direction
        """
        #Get the closest person
        closest_pos = self.get_closest_zombie()

        #Get the direction of the closest person
        direction_vector = self.get_next_moving_direction(closest_pos)

        #Compute new position
        magnitude = self.speed * self.model.time_step
        next_pos = (self.pos[0] + magnitude*direction_vector[0],
                    self.pos[1] + magnitude*direction_vector[1])

        #Check if that position is allowed and changed it
        if not self.model.grid.out_of_bounds(next_pos):
            self.model.grid.move_agent(self, next_pos)

    def step(self):
        self.move_next_point()
