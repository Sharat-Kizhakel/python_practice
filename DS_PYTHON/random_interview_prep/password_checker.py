import string


def CheckPassword(str, n):

    if n < 4:
        return 0
    global isno
    isno = False

    for i in str:
        if i.isdigit():
            isno = True
        if i == " " or i == '/':
            return 0
    if not isno:
        return 0

    upper_let = string.ascii_uppercase

    final_upper_let = [True for i in str for j in upper_let if i == j]
    print(final_upper_let)
    if not any(final_upper_let):
        return 0
    if str[0].isdigit():
        return 0

    else:
        return 1


password = input("Enter password:")
print(CheckPassword(password, len(password)))
