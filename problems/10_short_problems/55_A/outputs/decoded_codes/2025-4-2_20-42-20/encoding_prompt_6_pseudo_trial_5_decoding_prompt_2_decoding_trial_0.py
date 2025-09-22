# Input: 
n = int(input())  # taking an integer input for the size of the array

# Initialization
isAlive = [True] * n  # Initialize an array 'isAlive' of size n with all values set to True
currentIndex = 0
stepCount = 1

# Elimination Process
while stepCount <= 500000:
    if isAlive[currentIndex]:  # Check if the current position is still alive
        isAlive[currentIndex] = False  # Mark this position as eliminated
    stepCount += 1  # Increment stepCount
    currentIndex = (currentIndex + stepCount) % n  # Update currentIndex with wrap around

# Final Check
remaining = [alive for alive in isAlive if alive]  # Create a list of all alive positions

if len(remaining) == 0:  # If there are no alive positions left
    print("YES")  # Output "YES" (no one is alive)
else:
    print("NO")  # Output "NO" (there are still people alive)
