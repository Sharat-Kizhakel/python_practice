# # using with closes the file automatically
# try:
#     with open('test.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File was not found")


# reading file **************************

# text = "Writing to a file after a long time"
# with open('test1.txt', 'w') as file:
#     file.write(text)

# appending
text = "Writing to a file"
with open('test1.txt', 'a') as file:
    file.write("Haha u coudnt overwrite me this time")
