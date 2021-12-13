import os
# nOTE:SINCE ITS A STRING NEED TO USE DOUBLE '\' IN PATH NAME
path = "C:\\Users\\admin\\Desktop\\py_trial.txt"
if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("File exists")
    elif os.path.isdir(path):
        print("File doesnt exist")
else:
    print("Location doesnt exist")
