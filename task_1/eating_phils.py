from threading import Semaphore, Lock, Thread
import random
from time import sleep


forks = []

for i in range(5):
    forks.append(Lock())


def eating_philosopher(id):
    fork_1 = forks[id-1]
    fork_2 = forks[id]
    while True:
        timeout = random.random()
        fork_1_is_taken = fork_1.acquire(timeout=timeout)
        fork_2_is_taken = fork_2.acquire(timeout=timeout)

        if fork_1_is_taken and fork_2_is_taken:
            print(f"Philosopher {id} is eating")
            sleep(random.random()*2)
            fork_2.release()
            fork_1.release()
        else:
            if fork_1_is_taken:
                fork_1.release()
            if fork_2_is_taken:
                fork_2.release()
        #sleep(1)   # Отправляю философов спать, чтобы дать возможность другим поесть

for i in range(5):
    Thread(target=eating_philosopher, args=(i,)).start()

