# Start the program

# Get user input
totalCount = int(input())

# Initialize the list
isMarked = [True] * totalCount

# Set counters
currentStep = 1
index = 0

# Processing loop
while currentStep <= 500000:
    if isMarked[index]:
        isMarked[index] = False  # mark this position as processed
    currentStep += 1
    index = (index + currentStep) % totalCount  # wrap around to the beginning if needed

# Check results
remainingTrue = [value for value in isMarked if value]

# Determine output
if len(remainingTrue) == 0:
    print("YES")
else:
    print("NO")

# End the program
