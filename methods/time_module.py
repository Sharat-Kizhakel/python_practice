import time

# epoch=when computer thinks time began arg is how many secs after epoch in this case 0
print(time.ctime(0))

print(time.time())  # no of elapsed s since epoch

time_obj = time.localtime()
print(time_obj)
local_time = time.strftime("%B %d %Y %H:%M:%S", time_obj)
print(local_time)

time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)
