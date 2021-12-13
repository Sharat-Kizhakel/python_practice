def findCount(arr, length, num, diff):
    global found_less
    global c
    c = 0
    found_less = True
    for ele in arr:
        if abs(ele - num) <= diff:
            c += 1
            found_less = False
    if found_less is True:
        return -1
    else:
        return c


n = int(input("Enter array size:"))
num = int(input("Enter num:"))
diff = int(input("Enter the diff:"))
arr = []
for i in range(n):
    arr.append(int(input("Enter array element")))
print(findCount(arr, len(arr), num, diff))
