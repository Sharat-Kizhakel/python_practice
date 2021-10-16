# #moving files
# import os

# source = "test.txt"
# destination = "C:\\Users\\admin\\Desktop\\py_trial.txt"

# try:
#     if os.path.exists(destination):
#         print("there is already a file there")
#     else:
#         os.replace(source, destination)
#         print(source+"was moved")
# except FileNotFoundError:
#     print(source+"was not found")

# deleting files
import os
import shutil
path = "test.txt"
path1 = "test_dir"
try:
    os.remove(path)  # delete a file
    os.rmdir(path1)  # delete an empty directory
   # shutil.rmtree(path1) #delete a directory contining files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:  # whi
    print("You do not have permission to delete that")
except OSError:
    print("You cant delete that using that function")
else:
    print(path+" was deleted")
