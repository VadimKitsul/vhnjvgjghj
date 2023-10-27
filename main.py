import random

class Animal:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.danger = 0
        self.alive = True

    def to_eat(self):
        print('Time to eat')
        self.danger += 100
        self.hunger += 100

    def to_sleep(self):
        print('Time to sleep')
        self.danger += 50
        self.hunger += 0

    def to_chill(self):
        print('Time to chill')
        self.danger -= 0
        self.hunger -= 0

    def is_alive(self):
        if self.danger < -0.5:
            print("Cant out...")
            self.alive = False
        elif self.hunger <=0:
            print('Description')
            self.alive = False
        elif self.danger > 5:
            print('Passed externally')
            self.alive = False

    def end_of_day(self):
        print(f'Hunger = {self.hunger}')
        print(f'Danger = {self.danger}')

    def live(self, day):
        s = f'Day {day} of {self.name} life'
        print(f'{s:=^50}')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_chill()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_eat()
        self.end_of_day()
        self.is_alive()

nick = Animal(name='Tiger')

for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)


import random

class Bird:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.danger = 0
        self.alive = True

    def to_eat(self):
        print('Time to eat')
        self.danger += 0
        self.hunger += 100

    def to_sleep(self):
        print('Time to sleep')
        self.danger += 0
        self.hunger += 0

    def to_chill(self):
        print('Time to chill')
        self.danger -= 0
        self.hunger -= 0

    def is_alive(self):
        if self.danger < -0.5:
            print("Cant out...")
            self.alive = False
        elif self.hunger <=0:
            print('Description')
            self.alive = False
        elif self.danger > 5:
            print('Passed externally')
            self.alive = False

    def end_of_day(self):
        print(f'Hunger = {self.hunger}')
        print(f'Danger = {self.danger}')

    def live(self, day):
        s = f'Day {day} of {self.name} life'
        print(f'{s:=^50}')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_chill()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_eat()
        self.end_of_day()
        self.is_alive()

nick = Animal(name='Sparrow')

for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)

import random

class Fish:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.danger = 100
        self.alive = True

    def to_eat(self):
        print('Time to eat')
        self.danger += 100
        self.hunger += 100

    def to_sleep(self):
        print('Time to sleep')
        self.danger += 100
        self.hunger += 30

    def to_chill(self):
        print('Time to chill')
        self.danger -= 100
        self.hunger -= 0

    def is_alive(self):
        if self.danger < -0.5:
            print("Cant out...")
            self.alive = False
        elif self.hunger <=0:
            print('Description')
            self.alive = False
        elif self.danger > 5:
            print('Passed externally')
            self.alive = False

    def end_of_day(self):
        print(f'Hunger = {self.hunger}')
        print(f'Danger = {self.danger}')

    def live(self, day):
        s = f'Day {day} of {self.name} life'
        print(f'{s:=^50}')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_chill()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_eat()
        self.end_of_day()
        self.is_alive()

nick = Animal(name='Shark')

for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)

import random

class Insect:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.danger = 0
        self.alive = True

    def to_eat(self):
        print('Time to eat')
        self.danger += 0
        self.hunger += 100

    def to_sleep(self):
        print('Time to sleep')
        self.danger += 0
        self.hunger += 0

    def to_chill(self):
        print('Time to chill')
        self.danger -= 0
        self.hunger -= 0

    def is_alive(self):
        if self.danger < -0.5:
            print("Cant out...")
            self.alive = False
        elif self.hunger <=0:
            print('Description')
            self.alive = False
        elif self.danger > 5:
            print('Passed externally')
            self.alive = False

    def end_of_day(self):
        print(f'Hunger = {self.hunger}')
        print(f'Danger = {self.danger}')

    def live(self, day):
        s = f'Day {day} of {self.name} life'
        print(f'{s:=^50}')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_chill()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_eat()
        self.end_of_day()
        self.is_alive()

nick = Animal(name='ant')

for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
