
queue = []


def enqueue():
    element = int(input("Enter the element to be enqueued:"))
    queue.append(element)  # using append cuz it adds element to the end
    print(element, "is added to queue")


def dequeue():
    if not queue:  # checking if queue is empty
        print("queue is empty")
    else:
        e = queue.pop(0)
        print("removed element is:", e)


def display():
    print(queue)


while True:
    print("Select the operation \n 1.add \n 2.remove \n 3.show \n 4.quit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        quit()
    else:
        print("Enter the correct operation")
