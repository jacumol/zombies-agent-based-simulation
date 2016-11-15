# -*- coding: UTF-8 -*-

#----Built-in packages----#
import math
from random import uniform

#----Installed packages----#
from mesa import Agent

#----Import Classes----#

class Zombie(Agent):
    """docstring for Zombie."""
    def __init__(self, unique_id, model, speed,
            observation_radius=30, trasnf_range=2):
        super().__init__(unique_id, model)
        self.speed = speed #Speed given in m/s
        self.observation_radius = observation_radius #Given in meters
        self.trasnf_range = trasnf_range

    def get_closest_person(self):
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
            #If it's a person, get the position and distance.
            if n.__class__.__name__ == "Person":
                distance = self.model.grid.get_distance(self.pos, n.pos)
                if distance < min_distance:
                    closest_pos = n.pos
                    min_distance = distance

        return closest_pos

    def get_next_moving_direction(self, nearest_person_pos=None):
        """
            Function that computes next direction according to where
            the nearest person is.
        """
        if nearest_person_pos is None:
            nearest_person_pos=(uniform(0.0, self.model.grid.x_max),
                                uniform(0.0, self.model.grid.y_max))

        vector = (nearest_person_pos[0] - self.pos[0],
                  nearest_person_pos[1] - self.pos[1])

        magnitude = math.sqrt(vector[0]**2 + vector[1]**2)
        if magnitude == 0.0:
            magnitude = 0.0000001

        direction_vector = (vector[0]/magnitude, vector[1]/magnitude)
        return direction_vector

    def move_next_point(self):
        """
            Function that moves the agent according to his speed and direction
        """
        #Get the closest person
        closest_pos = self.get_closest_person()

        #Get the direction of the closest person
        direction_vector = self.get_next_moving_direction(closest_pos)

        #Compute new position
        magnitude = self.speed * self.model.time_step
        next_pos = (self.pos[0] + magnitude*direction_vector[0],
                    self.pos[1] + magnitude*direction_vector[1])

        #Check if that position is allowed and changed it
        if not self.model.grid.out_of_bounds(next_pos):
            self.model.grid.move_agent(self, next_pos)

    def infect_persons(self):
        """Function that infects all the person that are close enought"""
        #Get all the agents in the observation radius
        neighbors = self.model.grid.get_neighbors(self.pos,
                self.trasnf_range, include_center=False)

        for n in neighbors:
            #If it's a person, get the position and distance.
            if n.__class__.__name__ == "Person":
                print("Someone has been bitten")
                unique_id = n.unique_id
                self.model.schedule.remove(n)
                self.model.grid._remove_agent(n.pos, n)


                speed = uniform(0.0, self.model.max_speed_zombie)
                z = Zombie(unique_id, self.model, speed)
                self.model.schedule.add(z)

                # Add the agent to the grid cell
                self.model.grid.place_agent(z, n.pos)


    def step(self):
        self.move_next_point()
        self.infect_persons()
