# Step 1: Read input from the user
totalNumbers = int(input())

# Step 2: Initialize a list with True values
statusList = [True] * totalNumbers

# Step 3: Set initial indices
currentIndex = 0
step = 1

# Step 4: Loop until the step limit is reached
while step <= 500000:
    # Check if the current status is True
    if statusList[currentIndex] == True:
        # Mark the current position as False
        statusList[currentIndex] = False
    
    # Increase the step count
    step += 1
    
    # Update the current index in a circular manner
    currentIndex = (currentIndex + step) % totalNumbers

# Step 5: Check the remaining True values
remainingTrueValues = [value for value in statusList if value]

# Step 6: Output the result based on the remaining True values
if len(remainingTrueValues) == 0:
    print("YES")
else:
    print("NO")
