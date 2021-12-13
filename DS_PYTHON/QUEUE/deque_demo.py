# deque is there in collections module of python
import collections
import queue  # demoing the queue module as well

q = collections.deque()
q.appendleft(10)
q.appendleft(30)
q.appendleft(20)
print(q)
q.pop()
print(q)
print("--------------------")
q = queue.Queue(maxsize=5)
q.put(10)
q.put(50)
q.put(30)
q.put(40)
q.put(60)

q.get_nowait()
q.get()
q.get()

# even after deleting  when empty there is no error message
