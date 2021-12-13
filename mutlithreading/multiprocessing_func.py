# py multiprocessing
#
#
# multiprocessing=running tasks or processes(NOT NOT THREADS!!!!) in parallel on different CPU cores,bypasses GIL used for threading
# multiprocessing vs multithreading
# multiprocessing:better for cpu bound tasks (heavy cpu usage)
# multithreading:better for io bound tasks (waitng around)


from multiprocessing import Process, cpu_count
import time
# heavy cpu usage function


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    a = Process(target=counter, args=(500000000,))
    # must add , in arg list otherwise error
    b = Process(target=counter, args=(500000000,))
    print(cpu_count())
    a.start()
    b.start()
    a.join()  # suspends calling method until called method terminates(IN THIS CASE counter )
    b.join()
    print("finished in:", time.perf_counter(), "seconds")


if __name__ == '__main__':
    main()
