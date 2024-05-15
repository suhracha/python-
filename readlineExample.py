# Open the file in read mode
file = open("2.txt", "r")
# Read the first line
line1 = file.readline()
print(line1)
# Read the second line
line2 = file.readline()
print(line2)
# Close the file
file.close()