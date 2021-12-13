# basic stack operation

stack = []
global n


def push():
    if len(stack) == n:
        print("STACK is full")
    else:
        element = input("Enter an element:")
        stack.append(element)
        global top
        print(stack)


def pop_element():
    if not stack:  # empty lists are considered false in python
        print("stack is empty")
    else:
        popped_ele = stack.pop(-1)
        print("removed element is {}".format(popped_ele))
        print(stack)


def peek():
    print(stack[-1])


global user_continue
user_continue = True

n = int(input("Enter the limit of the stack:"))
while user_continue:
    print("select operation:")
    print("1.push 2.pop 3.peek 4.quit:")
    user_choice = int(input())
    if user_choice == 1:
        push()
    elif user_choice == 2:
        pop_element()
    elif user_choice == 3:
        peek()
    elif user_choice == 4:
        quit()
    else:
        print("Enter the correct operation")
