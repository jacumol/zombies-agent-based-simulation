# -*- coding: UTF-8 -*-

#----Built-in packages----#
from __future__ import division
import math
from random import uniform

#----Installed packages----#

#----Import Classes----#
from person import Person
from zombie import Zombie

class Zombieland(object):
    """docstring for Zombieland"""
    def __init__(self, num_persons=10, num_zombies=1,
                 allowed_area=(10.0, 10.0)):
        super(Zombieland, self).__init__()
        self.num_persons = num_persons
        self.num_zombies = num_zombies
        self.persons = []
        self.zombies = []
        self.allowed_area = allowed_area

    def create_person(self, id_person):
        """
            Function that creates a person
        """
        max_speed_person = 2.0
        speed = uniform(0.0, max_speed_person)
        pos = (uniform(0.0, self.allowed_area[0]),
               uniform(0.0, self.allowed_area[1]))

        p = Person(id_person, speed, pos, self.allowed_area)
        return p

    def create_zombie(self, id_person):
        """
            Function that creates a zombie
        """
        max_speed_zombie = 0.5
        trasnf_range = 2
        speed = uniform(0.0, max_speed_zombie)
        pos = (uniform(0.0, self.allowed_area[0]),
               uniform(0.0, self.allowed_area[1]))

        z = Zombie(trasnf_range, id_person, speed, pos, self.allowed_area)
        return z

    def populate_city(self):
        """
            Function that poblates zombieland
        """
        for i in range(self.num_persons):
            id_person = i
            p = self.create_person(id_person)
            self.persons.append(p)


        for i in range(self.num_zombies):
            id_person = i
            z = self.create_zombie(id_person)
            self.zombies.append(z)

    def get_distance(self, pos0, pos1):
        """
            Fucntion that computes the distance between two points.
        """
        diff_x = pos0[0]-pos1[0]
        diff_y = pos0[1]-pos1[1]
        distance = math.sqrt(diff_x**2 + diff_y**2)
        return distance

    def get_nearest_zombie_position(self, person):
        """
            Fucntion that computer the nearest zombie to a specific person.
        """
        if len(self.zombies) == 0:
            pos = (uniform(0.0, self.allowed_area[0]),
                   uniform(0.0, self.allowed_area[1]))
        else:
            distances = []
            for z in self.zombies:
                dist = self.get_distance(person.pos, z.pos)
                distances.append(dist)

            index = distances.index(min(distances))
            pos = self.zombies[index].pos

        return pos

    def get_nearest_person_position(self, zombie):
        """
            Fucntion that computer the nearest zombie to a specific person.
        """
        if len(self.persons) == 0:
            pos = (uniform(0.0, self.allowed_area[0]),
                   uniform(0.0, self.allowed_area[1]))
        else:
            distances = []
            for p in self.persons:
                dist = self.get_distance(zombie.pos, p.pos)
                distances.append(dist)

            index = distances.index(min(distances))
            pos = self.persons[index].pos

        return pos

    def trasnform_persons(self, zombie):
        """
            Function that checks if any person is transform after a
            zombie moves
        """
        if len(self.persons) > 0:
            for p in self.persons:
                dist = self.get_distance(zombie.pos, p.pos)
                if dist <= zombie.trasnf_range:
                    print "Some has been bitten"
                    #Remove that person
                    self.persons.remove(p)

                    #Create a new zombie
                    id_person = len(self.zombies)
                    z = self.create_zombie(id_person)
                    self.zombies.append(z)

    def move_zombies(self, time_step):
        """Function that moves the zombies"""
        for z in self.zombies:
            nearest_person_pos = self.get_nearest_person_position(z)
            z.move_next_point(time_step, nearest_person_pos)
            self.trasnform_persons(z)

    def move_persons(self, time_step):
        """Function that moves the zombies"""
        for p in self.persons:
            nearest_zombie_pos = self.get_nearest_zombie_position(p)
            p.move_next_point(time_step, nearest_zombie_pos)

    def print_population_position(self):
        """Function that print current positions"""
        pos_persons = ""
        for p in self.persons:
            pos_persons += str(p.pos)

        pos_zombies = ""
        for z in self.zombies:
            pos_zombies += str(z.pos)

        print pos_persons
        print pos_zombies

    def let_the_game_begins(self):
        """
            Function that iterates over the time
        """
        #Time in secons
        time_step = 0.1
        t = 0
        print "N zombies:", len(self.zombies)
        print "N persons:", len(self.persons)
        i = 0
        while len(self.persons):
            self.move_zombies(time_step)
            self.move_persons(time_step)
            if i%500 == 0:
                print "Seconds:", i*time_step
                print "N persons:", len(self.persons)
                print "N zombies:", len(self.zombies)

            if i%1000 == 0:
                #self.print_population_position()
                pass
            i+=1



def main():
    zombieland = Zombieland(num_persons=1000, num_zombies=10,
                            allowed_area=(1000.0, 1000.0))
    zombieland.populate_city()
    zombieland.let_the_game_begins()


if __name__ == '__main__':
    main()
