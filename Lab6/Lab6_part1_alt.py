#student name:      Josiah Tsang
#student number:    74191248

import multiprocessing
from multiprocessing.connection import wait
import random #is used to cause some randomness 
import time   #is used to cause some delay to simulate thinking or eating times

def philosopher(id: int, chopstick: list): 
    """
       implements a thinking-eating philosopher
       id is used to identifier philosopher #id (id is between 0 to numberOfPhilosophers-1)
       chopstick is the list of semaphores associated with the chopsticks 
    """
    for _ in range(6): #to make testing easier, instead of a forever loop we use a finite loop
        
        def eatForAWhile():   #simulates philosopher eating time with a random delay
            print(f"DEBUG: philosopher{id} eating")
            time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
        
        def thinkForAWhile(): #simulates philosopher thinking time with a random delay
            print(f"DEBUG: philosopher{id} thinking")
            time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)

        leftChopstick = id
        rightChopstick = (id + 1) % 5      #5 is number of philosophers
        
        # print(f"The leftchopstick value of philosopher {id} is: {chopstick[leftChopstick].get_value()}")
        # print(f"The rightchopstick value of philosopher {id} is: {chopstick[rightChopstick].get_value()}")

        # philosopher asks permission from waiter to pick up both chopsticks
        while (chopstick[leftChopstick].get_value() == 0 and chopstick[rightChopstick].get_value() == 0):
            pass
        #to simplify, try statement not used here
        chopstick[leftChopstick].acquire()
        print(f"DEBUG: philosopher{id} has chopstick{leftChopstick}")
        chopstick[rightChopstick].acquire()
        print(f"DEBUG: philosopher{id} has chopstick{rightChopstick}")
   
        eatForAWhile()  #use this line as is
        
        print(f"DEBUG: philosopher{id} is to release chopstick{rightChopstick}")
        chopstick[rightChopstick].release()
        print(f"DEBUG: philosopher{id} is to release chopstick{leftChopstick}")
        chopstick[leftChopstick].release()

        thinkForAWhile()  #use this line as is

if __name__ == "__main__":
    semaphoreList = list()          #this list will hold one semaphore per chopstick
    numberOfPhilosophers = 5

    # each binary semaphore initialized to 1, with 1 indicating free and 0 indicating being used
    for i in range(numberOfPhilosophers):             
        semaphoreList.append(multiprocessing.Semaphore(1))    #one semaphore per chopstick

    philosopherProcessList = list()
    for i in range(numberOfPhilosophers): #instantiate all processes representing philosophers
        philosopherProcessList.append(multiprocessing.Process(target=philosopher, args=(i, semaphoreList)))
    for j in range(numberOfPhilosophers): #start all child processes
        philosopherProcessList[j].start()
    for k in range(numberOfPhilosophers): #join all child processes
        philosopherProcessList[k].join()

# https://en.wikipedia.org/wiki/Dining_philosophers_problem