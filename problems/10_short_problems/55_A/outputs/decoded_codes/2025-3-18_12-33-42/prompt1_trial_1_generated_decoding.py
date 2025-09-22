# Step 1: Read an integer n
n = int(input())

# Step 2: Initialize the isAvailable list
isAvailable = [True] * n  # creates a list of size n filled with True

# Step 3: Set Up Control Variables
index = 0
step = 1

# Step 4: Loop
while step <= 500000:
    if isAvailable[index]:  # Check if the current position is available
        isAvailable[index] = False  # Mark the position as not available
    step += 1  # Increment step by 1
    index = (index + step) % n  # Update index

# Step 5: Check for Availability
availablePositions = [i for i in range(n) if isAvailable[i]]  # List of available positions

# Step 6: Output
if len(availablePositions) == 0:
    print("YES")  # All positions are marked as not available
else:
    print("NO")   # At least one position is still available
