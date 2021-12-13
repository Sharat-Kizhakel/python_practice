# copying files

import shutil

shutil.copyfile('test.txt', "test1.txt")  # src,dest

# copyfile()=copies file contents
# copy()=copyfile()+ permission mode+desitination can be a directory
# copy2()=copy()+copies metadata
