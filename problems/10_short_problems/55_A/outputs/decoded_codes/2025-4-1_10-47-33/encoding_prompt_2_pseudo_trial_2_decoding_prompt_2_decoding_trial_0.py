# Begin the program

# Step 2: Read an integer value `n` from user input
n = int(input())

# Step 3: Create a list `isActive` of length `n`, initialized to True
isActive = [True] * n

# Step 4: Initialize `currentIndex` to 0
currentIndex = 0

# Step 5: Initialize `increment` to 1
increment = 1

# Step 6: While `increment` is less than or equal to 500000
while increment <= 500000:
    # Step 6.1: If `isActive[currentIndex]` is True
    if isActive[currentIndex]:
        # Set `isActive[currentIndex]` to False
        isActive[currentIndex] = False
    
    # Step 6.2: Increment `increment` by 1
    increment += 1
    
    # Step 6.3: Update `currentIndex`
    currentIndex = (currentIndex + increment) % n

# Step 7: Create `activeElements` list containing elements from `isActive` that are still True
activeElements = [value for value in isActive if value]

# Step 8: If length of `activeElements` is equal to 0
if len(activeElements) == 0:
    # Output "YES"
    print("YES")
# Step 9: Otherwise
else:
    # Output "NO"
    print("NO")

# End the program
