# Accept an integer input representing the size of the array
sizeOfArray = input()
arraySize = int(sizeOfArray)

# Initialize a boolean array of size 'arraySize' with all values set to True
arrayOfBooleans = [True] * arraySize

# Initialize the index variable for the boolean array
index = 0

# Initialize a counter variable starting from 1
counter = 1

# Loop for a maximum of 500000 iterations
while counter <= 500000:
    # If the current position in the boolean array is still True
    if arrayOfBooleans[index]:
        # Set the current position in the boolean array to False
        arrayOfBooleans[index] = False
    
    # Move to the next number by incrementing the counter
    counter += 1
    
    # Calculate the new index in a circular manner
    index = (index + counter) % arraySize

# Create a new list of elements from the boolean array that are still True
TrueValues = [value for value in arrayOfBooleans if value]

# Check if there are any True values left in the list
if len(TrueValues) == 0:
    # If there are no True values, print "YES"
    print("YES")
else:
    # If there are any True values, print "NO"
    print("NO")
