# Step 1: Begin the program.

# Step 2: Get an integer input from the user.
totalElements = int(input())

# Step 3: Create a list called booleanList, initialized to True.
booleanList = [True] * totalElements

# Step 4: Initialize currentIndex and increment.
currentIndex = 0
increment = 1

# Step 5: Start the loop for incrementing up to 500,000.
while increment <= 500000:
    # Step 5a: Check if the current position is True.
    if booleanList[currentIndex]:
        # Step 5ai: Set that position in booleanList to False.
        booleanList[currentIndex] = False
    
    # Step 5b: Increase increment by 1.
    increment += 1
    
    # Step 5c: Update currentIndex.
    currentIndex = (currentIndex + increment) % totalElements

# Step 6: Create a list for remaining True values.
remainingTrueValues = [value for value in booleanList if value]

# Step 7: Check the length of remainingTrueValues.
if len(remainingTrueValues) == 0:
    # Step 7a: Output "YES" if length is 0.
    print("YES")
else:
    # Step 7b: Output "NO" otherwise.
    print("NO")

# Step 8: End the program.
