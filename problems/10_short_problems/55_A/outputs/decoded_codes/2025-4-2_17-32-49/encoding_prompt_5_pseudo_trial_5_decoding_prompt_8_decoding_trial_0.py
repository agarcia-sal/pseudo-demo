# Start Program

# Input Section
n = int(input())

# Initialization
booleanList = [True] * n
currentIndex = 0
counter = 1

# Loop for Operations
while counter <= 500000:
    if booleanList[currentIndex]:
        booleanList[currentIndex] = False
        
    counter += 1
    currentIndex = (currentIndex + counter) % n

# Check Remaining True Values
remainingTrue = [val for val in booleanList if val]

if len(remainingTrue) == 0:
    print("YES")
else:
    print("NO")

# End Program
