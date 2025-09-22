# Start of the program

# Step 1: Input - Read an integer value called `totalNumbers`
totalNumbers = int(input())

# Step 2: Initialize a list called `isNumberAvailable`
# This list will indicate the availability of numbers from 0 to totalNumbers-1
isNumberAvailable = [True] * totalNumbers

# Step 3: Initialize the variables for the elimination process
stepCount = 1  # Tracks the current step in the elimination process
currentIndex = 0  # Tracks the current position in the `isNumberAvailable` list

# Step 4: Loop up to a maximum of 500,000 steps
while stepCount <= 500000:
    # Step 5: Check if the current index in the list is available
    if isNumberAvailable[currentIndex]:
        # Mark the number at currentIndex as not available
        isNumberAvailable[currentIndex] = False

    # Step 6: Increment the step count
    stepCount += 1

    # Update the current index using the formula
    currentIndex = (currentIndex + stepCount) % totalNumbers

# Step 7: Create a new list of available numbers
availableNumbers = [num for num in isNumberAvailable if num]

# Step 8: Check the availability of numbers and print the result
if len(availableNumbers) == 0:
    print("YES")  # All numbers have been eliminated
else:
    print("NO")  # There are still available numbers

# End of the program
