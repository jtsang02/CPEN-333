import multiprocessing
import time

def myProcess():
    print(f"Starting the child Process with pid: {multiprocessing.current_process().pid}")
    time.sleep(10)
    print("Child process terminating normally")
    
if __name__ == "__main__":
    p = multiprocessing.Process(target=myProcess, name="child")
    p.start()
    time.sleep(1)
    print("Main is to terminate the child process")
    p.terminate()
    print("Child process killed by main")
