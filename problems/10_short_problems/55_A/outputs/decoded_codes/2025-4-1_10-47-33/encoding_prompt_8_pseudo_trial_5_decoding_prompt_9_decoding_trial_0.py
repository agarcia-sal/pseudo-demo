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
    if isMarked[index]:  # If current index is still marked True
        isMarked[index] = False  # Mark this position as processed
    currentStep += 1  # Increment current step
    index = (index + currentStep) % totalCount  # Update index circularly

# Check results
remainingTrue = [entry for entry in isMarked if entry]  # List of unmarked entries

# Determine output
if len(remainingTrue) == 0:  # If no Entries are still True
    print("YES")
else:
    print("NO")

# End the program
