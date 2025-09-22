# Start

# Input
totalNumbers = int(input())

# Initialize
isNumberAvailable = [True] * totalNumbers
stepCount = 1
currentIndex = 0

# Loop
while stepCount <= 500000:
    if isNumberAvailable[currentIndex]:
        isNumberAvailable[currentIndex] = False
    
    stepCount += 1
    currentIndex = (currentIndex + stepCount) % totalNumbers

# Create a new list
availableNumbers = [num for num in isNumberAvailable if num]

# Check availability
if len(availableNumbers) == 0:
    print("YES")
else:
    print("NO")

# End
