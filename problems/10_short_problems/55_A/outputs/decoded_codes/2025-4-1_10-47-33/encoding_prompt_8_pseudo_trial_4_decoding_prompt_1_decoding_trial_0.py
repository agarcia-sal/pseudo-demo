# Read Input:
totalNumbers = int(input())

# Initialize List:
statusList = [True] * totalNumbers

# Set Initial Indices:
currentIndex = 0
step = 1

# Loop Until Limit Reached:
while step <= 500000:
    # If the value at statusList[currentIndex] is True,
    if statusList[currentIndex]:
        # Change statusList[currentIndex] to False.
        statusList[currentIndex] = False
        
    # Increase step by 1.
    step += 1
    
    # Update currentIndex to be the remainder of (currentIndex + step) divided by totalNumbers.
    currentIndex = (currentIndex + step) % totalNumbers

# Check Remaining True Values:
remainingTrueValues = [value for value in statusList if value]

# Output Result:
if len(remainingTrueValues) == 0:
    print("YES")
else:
    print("NO")
