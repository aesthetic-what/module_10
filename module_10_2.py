from threading import Thread
import time

class Knight(Thread):
    enemies = 100
    days = 0
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            self.days += 1
            time.sleep(1)
            if self.enemies >= 0:
                print(f"{self.name} сражается {self.days}..., осталось {self.enemies} воинов.")
                self.enemies -= self.power
            if self.enemies == 0:
                print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")

           

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print("Все битвы закончились!")