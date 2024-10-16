from threading import Thread
import requests
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        vragi = 100
        day = 0
        print(f'{self.name}, на нас напали!')
        while vragi > 0:
            sleep(1)
            vragi = vragi - self.power
            day += 1
            sleep(1)
            print(f'{self.name} сражается {day} дней, осталось {vragi} воинов.')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')

