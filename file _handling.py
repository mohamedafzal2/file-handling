# # append 
# # readline

# # write
# file_path = 'example.txt'

# with open(file_path,'w')as file:
#     file.write("Hello world!.\n")


# print(f"Data has been written to{file_path}.")



# # read 
# file_path = 'example.txt'
# with open(file_path,'r')as file:
#     data = file.read()
#     print(f"Data has been written to{file_path}.")
#     print(data)


# # append
# file_path = 'example.txt'

# # Appending data to the file
# with open(file_path, 'a') as file:  
#     file.write("\nThis is the new appended line.") 
#     print(f"Data has been appended to {file_path}.")

# with open(file_path, 'r') as file:  
#     print(f"Contents of {file_path}:")
#     print(data)


# Open a file in read and write mode
file = open('example.txt', 'r+')
print(file.read())
file.write(' This is appended text.')
file.close()

 # open a file in binary mode
file = open('PO.jpg','rb')
print(file.read)
file.close()