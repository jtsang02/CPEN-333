import multiprocessing as mp
import time

def myProcess():
    print("Starting the child Process")
    print(f"Child process started: {mp.current_process()} pid = {mp.current_process().pid}")
    time.sleep(3)
    print("Child process terminating ...")

# PID - process id

if __name__ == "__main__":
    print(f"Main process: {mp.current_process()} pid = {mp.current_process().pid}")
    p = mp.Process(target=myProcess, name="child")
    p.daemon = False                # non deamonic, child will terminate last
    p.start()
    print("Let's see if the child process continues to execute")
    time.sleep(1)                   # change to <= 3s to see main process terminate first
    print("Main process terminating ...")