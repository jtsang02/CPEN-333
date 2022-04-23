import threading as thread
import random

# reader - writer synchronization problem using 2 semaphores and 1 integer
# https://www.youtube.com/watch?v=p2XDhW5INOo&ab_channel=NesoAcademy
# https://docs.python.org/3/library/threading.html#semaphore-objects

wrt = thread.Semaphore()        # used by writers and readers for mutual exclusion for writer
mutex = thread.Semaphore()      # used by readers to ensure mutual exclusion for updating readCount 
readCount = 0                   # keep track of how many processse/threads are currently read
x = 0                           # shared memory

# define reader function
def reader():
    global readCount
    global x
    
    mutex.acquire()                 # always acquire mutex to update readcount variable 
    readCount += 1                  # number of readers has increased by 1
    print ("readCount value is: ", readCount)                  
    if (readCount == 1):            # at least 1 reader trying to read from shared memory
        wrt.acquire()               # acquire wrt semaphore, if writer tries to write it will not be able to acquire wrt
    mutex.release()                 # other readers can enter while the current reader is inside crit section
    
    # critical section
    print ("reader is reading")     # reading is performed
    
    mutex.acquire()                 # always acquire mutex to update readcount variable 
    readCount -= 1                  # decrement value of readcount variable

    print ("readCount value is: ", readCount)   
    if (readCount == 0):            # if no readers left in critical section
        wrt.release()               # writer can enter now that there is no more readers left
    mutex.release()                 # reader leaves
    print()

# define writer function
def writer():
    global readCount
    global x
    wrt.acquire()                           # entry section

    # critical section
    print ("writer is writing")             # writing is performed
    x += 1                                  # write on shared memory
    print ("Shared data, x:" , x)   

    print ("writer is releasing the lock")  # exit section
    wrt.release()
    print()

# main function
if __name__ == '__main__':
    for i in range(0, 10):
        randomNumber = random.randint(0, 100)   #Generate a Random number between 0 to 100
        if (randomNumber < 50):
            Thread1 = thread.Thread(target = reader)
            Thread1.start()
        else:
            Thread2 = thread.Thread(target = writer)
            Thread2.start()

Thread1.join()
Thread2.join()

print ("total times written: ", x)