# 1. Start

# 2. Input
n = int(input())

# 3. Initialize
isAvailable = [True] * n  # Create a list of n elements, all set to True
position = 0               # Initialize position to 0
step = 1                   # Initialize step to 1

# 4. Loop until step exceeds 500,000
while step <= 500000:
    if isAvailable[position]:  # If position is available
        isAvailable[position] = False  # Mark the position as unavailable
    step += 1  # Increment step by 1
    position = (position + step) % n  # Update position with wrap-around

# 5. Check for available positions
availablePositions = [p for p in isAvailable if p]  # List of available positions

# 6. Output Result
if len(availablePositions) == 0:  # If no available positions
    print("YES")  # All positions marked unavailable
else:
    print("NO")  # Some positions are still available

# 7. End
