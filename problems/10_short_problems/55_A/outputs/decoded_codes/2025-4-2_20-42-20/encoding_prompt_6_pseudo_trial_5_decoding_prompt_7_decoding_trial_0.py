# Input: Read the size of the array
n = int(input())

# Step 1: Initialization
# Create an array 'isAlive' of size n with all values set to True
isAlive = [True] * n
currentIndex = 0
stepCount = 1

# Step 2: Elimination Process
# Loop up to a maximum of 500,000 iterations
while stepCount <= 500000:
    # Check if the current index is still "alive"
    if isAlive[currentIndex]:
        # Mark as False (the person is eliminated)
        isAlive[currentIndex] = False
        
    # Increment stepCount by 1 for the next round
    stepCount += 1
    
    # Update currentIndex to the next position, wrapping around if needed
    currentIndex = (currentIndex + stepCount) % n

# Step 3: Final Check
# Create a new list 'remaining' containing all values from isAlive that are still True
remaining = [alive for alive in isAlive if alive]

# Output the results based on the length of 'remaining'
if len(remaining) == 0:
    print("YES")  # No one is alive
else:
    print("NO")  # There are still people alive
