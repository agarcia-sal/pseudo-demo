# Step 1: Start

# Step 2: Receive input
n = int(input())  # Read an integer from the user

# Step 3: Initialize list
statusList = [True] * n  # Create a boolean list with n elements initialized to True

# Step 4: Initialize variables
currentIndex = 0
increment = 1

# Step 5: Process list
while increment <= 500000:  # Loop while increment is less than or equal to 500,000
    if statusList[currentIndex]:  # Check if the current index in statusList is True
        statusList[currentIndex] = False  # Set that element in statusList to False
    increment += 1  # Increase increment by 1
    currentIndex = (currentIndex + increment) % n  # Update currentIndex, wrapping around with modulo

# Step 6: Check remaining values
remainingTrue = [value for value in statusList if value]  # Create a list of remaining True values

# Step 7: Generate output
if not remainingTrue:  # If remainingTrue is empty
    print("YES")  # Print "YES" if all values are False
else:
    print("NO")  # Print "NO" otherwise

# Step 8: End
