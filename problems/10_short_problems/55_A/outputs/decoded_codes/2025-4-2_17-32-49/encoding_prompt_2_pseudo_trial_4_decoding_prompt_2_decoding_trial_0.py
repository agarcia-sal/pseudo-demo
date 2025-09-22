# Start
# Input
n = int(input())

# Initialize
isAvailable = [True] * n
position = 0
step = 1

# Loop until step exceeds 500,000
while step <= 500000:
    if isAvailable[position]:
        isAvailable[position] = False  # Mark this position as unavailable
    step += 1
    position = (position + step) % n  # Update position with wrap-around

# Check for available positions
availablePositions = [x for x in isAvailable if x]

# Output Result
if len(availablePositions) == 0:
    print("YES")  # All positions are marked unavailable
else:
    print("NO")   # Some positions are still available
# End
