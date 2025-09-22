# Read the size input
size = int(input())

# Create a boolean list initialized to True
booleanList = [True] * size

# Initialize currentIndex and step
currentIndex = 0
step = 1

# Perform operations while step is less than or equal to 500000
while step <= 500000:
    if booleanList[currentIndex]:
        booleanList[currentIndex] = False
    step += 1
    currentIndex = (currentIndex + step) % size

# Create a list of remaining True values
remainingTrue = [value for value in booleanList if value]

# Check if there are any True values remaining and print the result
if len(remainingTrue) == 0:
    print("YES")
else:
    print("NO")
