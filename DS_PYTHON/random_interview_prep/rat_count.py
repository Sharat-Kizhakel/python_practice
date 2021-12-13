def rat_count(r, unit, n, arr):
    if arr is None:
        return -1
    else:

        global subtotal
        subtotal = 0
        for index, i in enumerate(arr):

            subtotal = subtotal + i

            if subtotal >= (r * unit):
                return index + 1
    return 0


print("r:", end="")
r = int(input())
print("unit:", end="")
unit = int(input())
print("n:", end="")
n = int(input())
print("arr:", end="")

# map applies function to each element of the list in this case making every element an int
arr = list(map(int, input().split()))
print(rat_count(r, unit, n, arr))
