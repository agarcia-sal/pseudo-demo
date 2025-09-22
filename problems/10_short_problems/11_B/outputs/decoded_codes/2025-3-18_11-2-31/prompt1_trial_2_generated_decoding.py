# Start Program

# Get Input:
targetValue = abs(int(input()))  # Read an integer input from the user

# Initialize Variables:
index = 0  # Set a counter variable 'index' to 0

# Loop Forever:
while True:  # While true, repeat the following steps
    # Calculate Sum:
    sumValue = (index * (index + 1)) // 2  # Compute the triangular number

    # Calculate Difference:
    difference = sumValue - targetValue  # Compute the difference

    # Check Conditions:
    if sumValue == targetValue:  # If 'sumValue' is equal to 'targetValue'
        print(index)  # Print the value of 'index'
        break  # Exit the loop
    elif sumValue > targetValue:  # Else if 'sumValue' is greater than 'targetValue'
        if difference % 2 == 0:  # If 'difference' is even
            print(index)  # Print the value of 'index'
            break  # Exit the loop
    
    # Increment Counter:
    index += 1  # Increase the value of 'index' by 1

# End Program
