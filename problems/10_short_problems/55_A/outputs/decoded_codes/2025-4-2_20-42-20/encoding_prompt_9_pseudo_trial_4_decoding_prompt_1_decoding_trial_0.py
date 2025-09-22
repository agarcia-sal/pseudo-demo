# Step 1: Receive Input
n = int(input())

# Step 2: Initialize Variables
booleanList = [True] * n  # Create a list of size n initialized to True
index = 0                  # Set the index to 0
counter = 1                # Set the counter to 1

# Step 3: Loop through a Range
while counter <= 500000:
    if booleanList[index]:  # If the value at booleanList[index] is True
        booleanList[index] = False  # Mark it as processed (set to False)
    
    counter += 1           # Increment counter by 1
    index = (index + counter) % n  # Update index using modulo to wrap around

# Step 4: Check for Remaining True Values
remainingTrueValues = [value for value in booleanList if value]  # List of remaining True values 

# Step 5: Determine Output
if len(remainingTrueValues) == 0:  # If there are no remaining True values
    print("YES")                   # Print "YES" 
else:
    print("NO")                    # Otherwise, print "NO"
