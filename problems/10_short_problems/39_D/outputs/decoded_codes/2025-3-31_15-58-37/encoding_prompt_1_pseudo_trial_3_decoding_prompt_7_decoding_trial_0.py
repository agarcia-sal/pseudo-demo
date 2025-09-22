def doMain():
    # Step 2: Input Handling
    firstInput = input()  # Read the first line of input
    secondInput = input()  # Read the second line of input
    
    # Split the input strings into lists
    firstList = firstInput.split()  # Create a list from the first input
    secondList = secondInput.split()  # Create a list from the second input
    
    # Step 3: Initialize Counter
    differenceCount = 0  # Initialize a counter for differences
    
    # Step 4: Comparison Loop
    for index in range(3):  # Loop through indices 0 to 2 (inclusive)
        valueA = int(firstList[index])  # Convert the element to an integer (first list)
        valueB = int(secondList[index])  # Convert the element to an integer (second list)
        
        # Check if the values from both lists are not equal
        if valueA != valueB:  
            differenceCount += 1  # Increment the counter if values are different

    # Step 5: Decision Making
    if differenceCount < 3:  # If differences are less than 3
        print("YES")  # Print YES if differences are acceptable
    else:
        print("NO")  # Print NO if differences exceed the limit

# Step 6: Execution Block
if __name__ == "__main__":  # Check if the script is run directly
    doMain()  # Call the main function
