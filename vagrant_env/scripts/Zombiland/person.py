# -*- coding: UTF-8 -*-

#----Built-in packages----#
from __future__ import division
import math
from random import uniform

#----Installed packages----#

#----Import PitMotion Classes----#

class Person(object):
    """docstring for Person"""
    def __init__(self, id_person, speed=1.0, pos=(0.0, 0.0),
                 allowed_area=(10.0, 10.0)):
        super(Person, self).__init__()
        self.id_person = id_person
        self.speed = speed #Speed given in m/s
        self.pos = pos
        #Area where the person can move starting from (0.0, 0.0)
        self.allowed_area = allowed_area

    def get_next_moving_direction(self, nearest_zombie_pos=None):
        """
            Function that computes next direction according to where
            the nearest zombie is.
        """
        if nearest_zombie_pos is None:
            nearest_zombie_pos=(uniform(-1.0, 1.0), uniform(-1.0, 1.0))

        vector = (self.pos[0]-nearest_zombie_pos[0], \
                  self.pos[1]-nearest_zombie_pos[1])
        magnitude = math.sqrt(vector[0]**2 + vector[1]**2)
        direction_vector = (vector[0]/magnitude, vector[1]/magnitude)
        return direction_vector

    def is_new_position_ok(self, next_pos):
        """Function that evaluates if the new position is allowed"""
        result = False
        if 0.0 <= next_pos[0] <= self.allowed_area[0] and \
                0.0 <= next_pos[1] <= self.allowed_area[1]:
            result = True

        return result


    def move_next_point(self, seconds, nearest_zombie_pos=None):
        """
            Function that moves the agent according to his speed and direction
        """
        direction_vector = self.get_next_moving_direction(nearest_zombie_pos)

        magnitude = self.speed * seconds
        theta = math.atan(direction_vector[0]/direction_vector[1])
        next_pos = (self.pos[0] + magnitude*math.cos(theta), \
                    self.pos[1] + magnitude*math.sin(theta))

        #Check if that position is allowed
        if self.is_new_position_ok(next_pos):
            self.pos = next_pos
            print
        else:
            print "No way out"

def main():
    p1 = Person(0)
    for i in range(100):
        p1.move_next_point(1)

if __name__ == '__main__':
    main()
