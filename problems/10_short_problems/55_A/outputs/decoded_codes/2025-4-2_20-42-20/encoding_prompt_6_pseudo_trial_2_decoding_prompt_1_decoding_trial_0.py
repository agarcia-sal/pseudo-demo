# BEGIN PROGRAM

# Read an integer input representing the size of the array
sizeOfArray = int(input())

# Initialize a boolean array with 'sizeOfArray' elements, all set to True
booleanArray = [True] * sizeOfArray

# Initialize two variables for tracking the current state
indexToUpdate = 0
stepCount = 1

# Continue the loop while stepCount is less than or equal to 500,000
while stepCount <= 500000:
    
    # Check if the current position in the boolean array is True
    if booleanArray[indexToUpdate] == True:
        
        # Set the current position to False, indicating it has been processed
        booleanArray[indexToUpdate] = False
    
    # Increment the step count
    stepCount += 1
    
    # Update the index to the next position in the array using modulo operation
    indexToUpdate = (indexToUpdate + stepCount) % sizeOfArray

# Create a new list that contains all elements from booleanArray that are still True
filteredList = [element for element in booleanArray if element]

# Check if the filtered list is empty
if len(filteredList) == 0:
    
    # If the filtered list is empty, output "YES"
    print("YES")
    
else:
    
    # If the filtered list is not empty, output "NO"
    print("NO")

# END PROGRAM
