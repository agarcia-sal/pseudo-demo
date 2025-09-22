# Initialize Input
n = abs(int(input()))  # Get an absolute integer input value 'n' from the user

# Set Initial Values
index = 0

# Repeat Until Found
while True:  # Create an infinite loop that continues until a solution is found
    # Calculate Sum
    sumUpToIndex = (index * (index + 1)) // 2  # Calculate sum of the first 'index' integers

    # Determine the Difference
    difference = sumUpToIndex - n  # Calculate the difference

    # Check for Equality
    if sumUpToIndex == n:  # If the sum equals 'n'
        print(index)  # Print the current 'index'
        break  # Exit the loop

    # Check for Greater Than Condition
    if sumUpToIndex > n:  # If the sum is greater than 'n'
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # Print the current 'index'
            break  # Exit the loop

    # Increment Index
    index += 1  # Increase 'index' by 1 to check the next integer
