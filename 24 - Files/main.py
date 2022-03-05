# 219 Open, Read, Write, Append
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# alternative, which closes automatically
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# writing - default mode is readonly
# if file does not exist: create a new one
with open("my_file.txt", mode="w") as file:
    file.write("New Text.")

# append- mode a enables no deleting, but appending
with open("my_file.txt", mode="a") as file:
    file.write("\nNew Text.")