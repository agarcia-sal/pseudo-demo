# Start of the program

# Step 2: Get user input
totalCount = int(input())  # Read an integer from user input

# Step 3: Initialize the list
isMarked = [True] * totalCount  # Create a list with totalCount entries, all set to True

# Step 4: Set counters
currentStep = 1  # Step counter starts from 1
index = 0  # Initialize index to 0

# Step 5: Processing loop
while currentStep <= 500000:  # Iterate until currentStep exceeds 500000
    if isMarked[index]:  # If the current index is True (unmarked)
        isMarked[index] = False  # Mark this position as processed by setting it to False
    currentStep += 1  # Increment the step counter
    index = (index + currentStep) % totalCount  # Update the index, wrap around using modulo

# Step 6: Check results
remainingTrue = [x for x in isMarked if x]  # Create a list of entries that are still True

# Step 7: Determine output
if len(remainingTrue) == 0:  # If there are no remaining unmarked entries
    print("YES")  # Output "YES"
else:  # Otherwise, if there are still True entries
    print("NO")  # Output "NO"

# End of the program
