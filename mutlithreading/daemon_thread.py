# daemon thread= a thread that runs in the background,not important for program to run
# your program will not wait for daemon threads to complete before exiting
# DAEMON THREAD CONTINUES RUNNING UNTIL ALL NON DAEOMON THREADS HAVE COMPLELETED THEIR TASKS
# non-daemon threads cannot be normally killed,stay alive until task is complete and then exit
# eg background tasks,garbage collection,*waiting for input,long running process


import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for", count, "seconds")


# non-daemon thread we wont be close it unless we kill terminal
# this is a daemon thread
# x = threading.Thread(target=timer)
# x.start()
# therefore we convert the thread to daemon threa
# this will ensure that we exit when there arent any non daemon threads alive
x = threading.Thread(target=timer, daemon=True)
x.start()
print(x.isDaemon())  # checking if x is a daemon thread
# non daemon thread
answer = input("Do you wish to exit?")
# so in this program we can exit only once we have completed the non daemon thread's task
# i.e getting a response to asking for input
