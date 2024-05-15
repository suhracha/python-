# Open the file in read mode
file = open("2.txt", "r")
# Read all lines
lines = file.readlines()
# Close the file
file.close()
# Print each line
for line in lines:
    print(line)
