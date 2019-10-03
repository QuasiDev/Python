from sys import argv

# Declarations of variables
script, filename = argv

# Passing value to file and open the file
file = open(filename)

# User feedback and print contents of the file
print(f"Contents of {filename}: ")
print(file.read())

# Prompting for the filename again
print("Type the filename again: ")
filename_again = input('> ')

# Pass value to file_again and open the file
file_again = open(filename_again)

# Print contents of the file
print(file_again.read())