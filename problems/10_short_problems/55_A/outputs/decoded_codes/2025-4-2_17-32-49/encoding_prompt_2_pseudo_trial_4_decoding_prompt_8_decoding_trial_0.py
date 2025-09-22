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
        isAvailable[position] = False  # Mark as unavailable
    step += 1
    position = (position + step) % n  # Update position with wrapping

# Check for available positions
availablePositions = [i for i in isAvailable if i]

# Output Result
if len(availablePositions) == 0:
    print("YES")  # all positions are marked unavailable
else:
    print("NO")   # some positions are still available

# End
