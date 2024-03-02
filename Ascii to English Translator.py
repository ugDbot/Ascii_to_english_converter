# Code to take input of a list
# from the user.

# Take input of the size of the list
n = int (input ("Enter number of ascii elements: "))

# Declare an empty list
list = []

# Iterate for n times take inputs
for i in range (n):
    # Take input of ith element as x.
    x = int(input())
    # Append 'x' to the list.
    list.append(x)

# Create ascii converter variable
ascii_result_string = ""

# iterate the values and convert to ascii
for ascii_value in list:
    ascii_result_string += chr(ascii_value)

# Print the list
print("Translating ascii to english...")
print("Results:", ascii_result_string)
