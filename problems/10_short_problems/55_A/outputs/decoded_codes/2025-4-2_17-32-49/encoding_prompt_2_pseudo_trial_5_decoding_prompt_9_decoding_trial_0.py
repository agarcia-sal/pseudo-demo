# Start the program

# Input Requirement: Read an integer value denoting the size
totalElements = int(input())

# Initialize the list and variables
isActive = [True] * totalElements  # Create a list of size totalElements with all elements set to True
index = 0  # To track the current position in the list
step = 1   # To track the number of steps taken

# Loop while step is less than or equal to 500,000
while step <= 500000:
    # Check if the element at the current index is still True
    if isActive[index]:
        isActive[index] = False  # Set that element to False (inactive)

    step += 1  # Increase the step variable to move to the next step
    index = (index + step) % totalElements  # Update the index with wrapping around if necessary

# Filter Active Elements: Create a new list of only active elements
activeElements = [element for element in isActive if element]

# Output Requirement: Check the length of activeElements
if len(activeElements) == 0:
    print("YES")  # All elements have been marked inactive
else:
    print("NO")   # There are still active elements
