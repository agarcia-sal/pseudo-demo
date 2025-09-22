# Start by reading an integer input which represents a number called "totalCount".
totalCount = int(input())

# Create an array named "booleanArray" of size "totalCount", initializing all values to True.
booleanArray = [True] * totalCount

# Initialize two variables: incrementValue and index.
incrementValue = 1  # This will control the loop iterations.
index = 0           # This will track the current position in the booleanArray.

# Begin a loop that continues as long as incrementValue is less than or equal to 500,000.
while incrementValue <= 500000:
    # Check if the current position in the booleanArray (at index) holds a value of True.
    if booleanArray[index]:
        # Change the value at that position (index) in booleanArray to False.
        booleanArray[index] = False
    
    # Increase incrementValue by 1.
    incrementValue += 1
    
    # Update index by adding incrementValue to it and taking the modulus with totalCount.
    index = (index + incrementValue) % totalCount

# Create a new list called "trueValues" which contains all the positions in booleanArray that are still True.
trueValues = [i for i, value in enumerate(booleanArray) if value]

# Check the size of "trueValues".
if len(trueValues) == 0:
    # If trueValues is empty, print "YES".
    print("YES")
else:
    # Otherwise, print "NO".
    print("NO")
