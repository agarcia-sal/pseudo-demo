def doMain():
    # Read input values
    input1 = input()  # First line of input
    input2 = input()  # Second line of input
    
    # Split input strings into lists
    list1 = input1.split()  # Split input1 into words
    list2 = input2.split()  # Split input2 into words
    
    # Initialize the result counter
    mismatchCount = 0

    # Compare corresponding elements in both lists
    for index in range(3):  # Loop through the first three elements
        value1 = int(list1[index])  # Convert list1[index] to integer
        value2 = int(list2[index])  # Convert list2[index] to integer
        
        # Check for mismatch
        if value1 != value2:  # If values are not equal
            mismatchCount += 1  # Increment the mismatch counter
        
    # Determine if the number of mismatches is less than 3
    if mismatchCount < 3:  # If mismatches are less than 3
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO

# Main entry point
doMain()  # Call the main function
