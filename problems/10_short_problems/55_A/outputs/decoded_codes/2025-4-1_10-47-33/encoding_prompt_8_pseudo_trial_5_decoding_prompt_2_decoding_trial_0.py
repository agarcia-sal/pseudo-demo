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
    index = (index + currentStep) % totalCount  # wrap around to the beginning of the list if needed

# Check results
remainingTrue = [mark for mark in isMarked if mark]

# Determine output
if len(remainingTrue) == 0:  # if remainingTrue is empty
    print("YES")
else:
    print("NO")

# End the program
