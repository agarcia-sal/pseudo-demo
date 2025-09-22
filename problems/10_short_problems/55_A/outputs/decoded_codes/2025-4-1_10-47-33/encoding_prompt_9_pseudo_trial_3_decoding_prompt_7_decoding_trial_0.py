# Start of the program

# Step 2: Receive Input
n = int(input())  # Read the size of the list from the user

# Step 3: Initialize List
statusList = [True] * n  # Create a boolean list initialized to True

# Step 4: Initialize Variables
currentIndex = 0  # Variable to keep track of the current index
increment = 1  # Variable to control the increment

# Step 5: Process List
while increment <= 500000:  # Loop to process up to 500,000 increments
    if statusList[currentIndex]:  # Check if the current index is True
        statusList[currentIndex] = False  # Change it to False
    
    increment += 1  # Increase the increment

    # Update the current index, wrapping around using modulo n
    currentIndex = (currentIndex + increment) % n

# Step 6: Check Remaining Values
remainingTrue = [value for value in statusList if value]  # List of remaining True values

# Step 7: Generate Output
if not remainingTrue:  # If the list of remaining True values is empty
    print("YES")  # All values have been changed to False
else:
    print("NO")  # There are still True values in the list

# End of the program
