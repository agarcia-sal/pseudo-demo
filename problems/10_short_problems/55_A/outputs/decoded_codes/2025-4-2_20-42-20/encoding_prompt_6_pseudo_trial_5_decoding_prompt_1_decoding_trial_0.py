# Input: 
n = int(input())  # Read an integer value representing the size of the array

# Initialization
isAlive = [True] * n  # Initialize an array of size n with all values set to True
currentIndex = 0
stepCount = 1

# Elimination Process
while stepCount <= 500000:
    if isAlive[currentIndex]:  # If isAlive[currentIndex] is True
        isAlive[currentIndex] = False  # Mark isAlive[currentIndex] as False (the person is "eliminated")
    
    stepCount += 1  # Increment stepCount by 1
    currentIndex = (currentIndex + stepCount) % n  # Update currentIndex to (currentIndex + stepCount) modulo n

# Final Check
remaining = [x for x in isAlive if x]  # Create a new list containing all values from isAlive that are still True

if len(remaining) == 0:  # If the length of 'remaining' is 0
    print("YES")  # Output "YES" (no one is alive)
else:
    print("NO")  # Output "NO" (there are still people alive)
