# Step 1: Start by reading an integer input which represents totalCount.
totalCount = int(input())

# Step 2: Create an array named booleanArray of size totalCount, initializing all values to True.
booleanArray = [True] * totalCount

# Step 3: Initialize two variables
incrementValue = 1  # This will control loop iterations
index = 0           # This will track the current position in booleanArray

# Step 4: Begin a loop that continues as long as incrementValue <= 500,000
while incrementValue <= 500000:
    # Check if the current position in booleanArray at index holds a value of True
    if booleanArray[index]:
        # Change the value at that position in booleanArray to False
        booleanArray[index] = False
    
    # Increase incrementValue by 1
    incrementValue += 1
    
    # Update index by adding incrementValue and taking modulus with totalCount
    index = (index + incrementValue) % totalCount

# Step 5: Create a new list called trueValues which contains all positions in booleanArray that are still True
trueValues = [i for i in range(totalCount) if booleanArray[i]]

# Step 6: Check the size of trueValues
if len(trueValues) == 0:
    print("YES")  # If trueValues is empty, print "YES"
else:
    print("NO")   # Otherwise, print "NO"
