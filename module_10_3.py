from threading import Thread, Lock
from random import randint
import time


class Bank():
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            random_sum = randint(50, 500)
            self.balance += random_sum
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {random_sum}.\n Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            random_minus = randint(50, 500)
            print(f'Запрос на {random_minus}')
            if random_minus <= self.balance:
                self.balance -= random_minus
                print(f'Снятие: {random_minus}.\nБаланс: {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            
bk = Bank()
tr1 = Thread(target=Bank.deposit, args=(bk,))
tr2 = Thread(target=Bank.take, args=(bk,)) 

tr1.start()
tr2.start()

tr1.join()
tr2.join()

print(f'Итоговый счет: {bk.balance}')