from threading import Semaphore, Lock, Thread
import random
from time import sleep


forks = []

waiter_allow = Semaphore(value=2)

for i in range(5):
    forks.append(Lock())


def eating_philosopher(id):
    while True:
        with waiter_allow:
            timeout = random.random()
            fork_1 = forks[id-1].acquire(timeout=timeout)
            fork_2 = forks[id].acquire(timeout=timeout)
            if fork_1 and fork_2:
                print(f"Philosopher {id} is eating")
                sleep(random.random()*2)
                forks[id].release()
                forks[id-1].release()
            else:
                if fork_1:
                    forks[id-1].release()
                if fork_2:
                    forks[id].release()
        sleep(1)   # Отправляю философов спать, чтобы дать возможность другим поесть

for i in range(5):
    Thread(target=eating_philosopher, args=(i,)).start()

