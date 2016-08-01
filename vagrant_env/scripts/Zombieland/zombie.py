# -*- coding: UTF-8 -*-

#----Built-in packages----#
from __future__ import division
import math
from random import uniform

#----Installed packages----#

#----Import Classes----#
from person import Person

class Zombie(Person):
    """docstring for Zombie"""
    def __init__(self, trasnf_range, *args, **kw):
        super(Zombie, self).__init__(*args, **kw)
        #It's the distance in meters where he can transform someone
        self.trasnf_range = trasnf_range

    def get_next_moving_direction(self, nearest_person_pos=None):
        """
            Function that computes next direction according to where
            the nearest person is.
        """
        if nearest_person_pos is None:
            nearest_person_pos=(uniform(-1.0, 1.0), uniform(-1.0, 1.0))

        vector = (nearest_person_pos[0]-self.pos[0],
                  nearest_person_pos[1]-self.pos[1])
        magnitude = math.sqrt(vector[0]**2 + vector[1]**2)
        direction_vector = (vector[0]/magnitude, vector[1]/magnitude)
        return direction_vector
