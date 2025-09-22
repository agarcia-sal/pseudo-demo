def doMain():
    # Read input values
    input1 = input()  # Read the first input
    input2 = input()  # Read the second input
    
    # Split input strings into lists
    list1 = input1.split()  # Split the first input into words
    list2 = input2.split()  # Split the second input into words
    
    # Initialize the result counter
    mismatchCount = 0

    # Compare corresponding elements in both lists
    for index in range(3):  # Loop through first three elements
        if index < len(list1) and index < len(list2):  # Check if the index is within bounds
            value1 = int(list1[index])  # Convert list1 element to integer
            value2 = int(list2[index])  # Convert list2 element to integer
            
            if value1 != value2:  # Check for mismatch
                mismatchCount += 1  # Increment the mismatch count

    # Determine if the number of mismatches is less than 3
    if mismatchCount < 3:
        print("YES")  # Output "YES" if mismatches are fewer than 3
    else:
        print("NO")  # Output "NO" otherwise

# Main entry point
doMain()
