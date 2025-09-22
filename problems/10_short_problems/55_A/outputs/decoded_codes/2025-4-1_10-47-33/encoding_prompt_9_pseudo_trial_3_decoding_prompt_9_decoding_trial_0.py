# Start of the program

# Receive Input:
n = int(input())  # Read an integer from the user to determine the size of the list

# Initialize List:
statusList = [True] * n  # Create a boolean list with n elements, all initialized to True

# Initialize Variables:
currentIndex = 0  # Set the current index to 0
increment = 1  # Set initial increment to 1

# Process List:
while increment <= 500000:  # Continue the loop while increment is less than or equal to 500,000
    if statusList[currentIndex]:  # Check if the current index in statusList is True
        statusList[currentIndex] = False  # Change that element to False
    
    increment += 1  # Increase increment by 1
    currentIndex = (currentIndex + increment) % n  # Update currentIndex and wrap around with modulus n

# Check Remaining Values:
remainingTrue = [value for value in statusList if value]  # Create a list of remaining True values

# Generate Output:
if not remainingTrue:  # If remainingTrue is empty (all are False):
    print("YES")  # Print YES
else:
    print("NO")  # Otherwise, print NO

# End of the program
