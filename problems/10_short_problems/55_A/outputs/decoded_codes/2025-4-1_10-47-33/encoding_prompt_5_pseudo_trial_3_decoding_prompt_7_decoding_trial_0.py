# Start of the program

# Step 1: Read a number from the user
numberOfElements = int(input())

# Step 2: Initialize an array of boolean values, all set to true
booleanArray = [True] * numberOfElements

# Step 3: Set initial counters
positionIndex = 0
stepCounter = 1

# Step 4: Loop until stepCounter exceeds 500000
while stepCounter <= 500000:
    # Step 5: Check if the current position in the array is true
    if booleanArray[positionIndex] == True:
        # Step 6: Set the current position in the array to false
        booleanArray[positionIndex] = False

    # Step 7: Increment the stepCounter
    stepCounter += 1

    # Step 8: Update positionIndex based on the stepCounter
    positionIndex = (positionIndex + stepCounter) % numberOfElements

# Step 9: Filter the booleanArray to find remaining true values
remainingTrueValues = [value for value in booleanArray if value]

# Step 10: Check if there are any true values left in the filtered list
if len(remainingTrueValues) == 0:
    # Step 11: Print "YES" if there are no true values left
    print("YES")
else:
    # Step 12: Print "NO" if there are still true values left
    print("NO")

# End of the program
