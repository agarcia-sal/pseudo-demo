# Input: n is an integer value representing the size of the array
n = int(input())

# Initialize an array 'isAlive' of size n with all values set to True
isAlive = [True] * n
currentIndex = 0
stepCount = 1

# Elimination process
while stepCount <= 500000:
    if isAlive[currentIndex]:  # Check if the person at currentIndex is alive
        isAlive[currentIndex] = False  # Mark as eliminated
    stepCount += 1  # Increment step count
    currentIndex = (currentIndex + stepCount) % n  # Update index with wrap around

# Create a new list 'remaining' containing all values from isAlive that are still True
remaining = [person for person in isAlive if person]

# Final check
if len(remaining) == 0:
    print("YES")  # Output indicating no one is alive
else:
    print("NO")  # Output indicating there are still people alive
