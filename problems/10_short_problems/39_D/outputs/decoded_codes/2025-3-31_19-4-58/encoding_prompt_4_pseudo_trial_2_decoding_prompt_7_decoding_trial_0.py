def doMain():
    # Read inputs for two sets of three integers
    firstInput = input()  # First input from the user
    secondInput = input()  # Second input from the user

    # Split inputs into lists of strings
    firstList = firstInput.split()  # Split the first input string into a list
    secondList = secondInput.split()  # Split the second input string into a list

    # Initialize a counter for mismatches
    mismatchCount = 0 

    # Loop through the first three elements of both lists
    for index in range(3):  # iterating from 0 to 2
        # Convert the string elements to integers
        firstValue = int(firstList[index])  # Convert the element from first list
        secondValue = int(secondList[index])  # Convert the element from second list
        
        # Check if the corresponding values are different
        if firstValue != secondValue:  # If values are not equal
            # Increment the mismatch count
            mismatchCount += 1  # Increase count of mismatches

    # Determine if the number of mismatches is less than 3
    if mismatchCount < 3:  # If mismatches are less than 3
        print("YES")  # Print YES if condition is met
    else:
        print("NO")  # Print NO if condition is not met

# Main execution
doMain()  # Call the function to execute
