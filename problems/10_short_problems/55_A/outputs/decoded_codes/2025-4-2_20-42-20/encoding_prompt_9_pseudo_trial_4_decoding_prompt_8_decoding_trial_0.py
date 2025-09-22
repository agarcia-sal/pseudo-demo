# Receive Input
n = int(input())

# Initialize Variables
booleanList = [True] * n
index = 0
counter = 1

# Loop through a Range
while counter <= 500000:
    if booleanList[index]:
        booleanList[index] = False  # Mark as processed
    counter += 1
    index = (index + counter) % n

# Check for Remaining True Values
remainingTrueValues = [value for value in booleanList if value]

# Determine Output
if len(remainingTrueValues) == 0:
    print("YES")
else:
    print("NO")
