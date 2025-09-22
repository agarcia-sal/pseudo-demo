# This program simulates the activation and deactivation of elements in a boolean list.
# It reads an integer input that represents the size of the list and processes it accordingly.

# Read an integer input that represents the size of the list
sizeOfList = int(input())

# Create a boolean list initialized to True, indicating all elements are active
booleanList = [True] * sizeOfList

# Initialize index variables
indexToCheck = 0
incrementValue = 1

# Loop until the increment value exceeds 500,000
while incrementValue <= 500000:
    
    # If the current position in the boolean list is still active (True), deactivate it
    if booleanList[indexToCheck]:
        booleanList[indexToCheck] = False  # Set the boolean list at the index to False
    
    # Move to the next increment value
    incrementValue += 1
    
    # Update the index to check, wrapping around if it exceeds the size of the list
    indexToCheck = (indexToCheck + incrementValue) % sizeOfList  # Calculate the new index

# Create a new list containing only the active elements (True) from the boolean list
activeElements = [element for element in booleanList if element]  # List comprehension to filter True values

# Check if there are any active elements left
if len(activeElements) == 0:  # Check if the active elements list is empty
    print('YES')  # Indicates that all elements have been deactivated
else:
    print('NO')  # Indicates that some elements remain active
