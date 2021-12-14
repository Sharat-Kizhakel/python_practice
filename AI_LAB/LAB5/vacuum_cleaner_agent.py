# LAB5 Implement vacuum cleaner agent.
def print_floor(floor, i, j):
    for m in range(len(floor)):
        for n in range(len(floor[0])):
            if(m == i and n == j):
                print("|{}|".format(floor[m][n]), end=" ")
            else:
                print("{}".format(floor[m][n]), end="  ")
        print(end="\n")
    print(end="\n")


def clean(floor):
    row_len = len(floor)
    for i in range(row_len):
        if i % 2 == 0:
            # on even floor we go left to right
            for j in range(len(floor[0])):
                if floor[i][j] == 1:
                    print("STATUS:DIRTY")
                    print_floor(floor, i, j)
                    floor[i][j] = 0
                    print("CLEANED:")
                    print_floor(floor, i, j)
                else:
                    print("STATUS:CLEAN")
                    print_floor(floor, i, j)
        else:
            # on odd floor right to left
            for j in range(len(floor[0]) - 1, -1, -1):
                if floor[i][j] == 1:
                    print("STATUS DIRTY:")
                    print_floor(floor, i, j)
                    floor[i][j] = 0
                    print("CLEANED:")
                    print_floor(floor, i, j)
                else:
                    print("STATUS:CLEAN")
                    print_floor(floor, i, j)
    print("ALL STATES CLEANED")
    return


def main():
    floor = []  # its gonna contain the different floors and their status if dirty or not
    row = int(input("enter the no of rows:"))
    col = int(input("Enter the no of columns:"))
    floor_row = []
    print("Enter 1 for dirty 0 for clean:")
    for i in range(row):
        for j in range(col):
            floor_row.append(int(input("Enter [{}][{}]:".format(i, j))))
        floor.append(floor_row)
        floor_row = []
    clean(floor)


main()
