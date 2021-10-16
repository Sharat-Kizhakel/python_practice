# thread=  flow of execution. Lke a sperate order of instructions.
# However each thread takes a turn running to achieve concurrency
# GIL=(GLOBAL INTERPRETER LOCK)
# allows only one thread to hold control of the Python interpreter
# cpu bound=program/task spends most of its time waiting for internal events (CPU intensive ) use MULTIPROCESSING
#
# io bound=program/task spends most of its time waiting for external events(user input) use MULTITHREADING

import threading
import time

# single threading approach
# def eat_breakfast():
#     time.sleep(3)
#     print("You eat bf")


# def drink_coffee():
#     time.sleep(4)
#     print("You drink coffee")


# def study():
#     time.sleep(5)
#     print("You are studying")
# here the main thread is in charge
# eat_breakfast()
# drink_coffee()
# study()

# multithreading approach
def eat_breakfast():
    time.sleep(3)
    print("You eat bf")


def drink_coffee():
    time.sleep(4)
    print("You drink coffee")


def study():
    time.sleep(5)
    print("You are studying")


# these are main thread responsibility
# thread for eating bf
x = threading.Thread(target=eat_breakfast, args=())
x.start()
# thread for coffeee
y = threading.Thread(target=drink_coffee, args=())
y.start()
# thread for studying
z = threading.Thread(target=study, args=())
z.start()

# thread synchronization
x.join()  # has to wait for thread1 to finish before it can proceed with the rest of the prog
y.join()
z.join()
# no of running threads
# this is the main thread responsibility
print(threading.active_count())  # will be 4 incl main thread
print(threading.enumerate())
print(time.perf_counter())
