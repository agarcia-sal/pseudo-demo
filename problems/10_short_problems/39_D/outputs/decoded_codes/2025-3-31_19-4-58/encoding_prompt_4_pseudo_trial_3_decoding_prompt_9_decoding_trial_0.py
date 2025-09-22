def doMain():
    # Initialize variables
    input1 = input()  # Read first line of input
    input2 = input()  # Read second line of input
    
    # Split the inputs into lists
    splitInput1 = input1.split()  # Split string into list by spaces
    splitInput2 = input2.split()  # Split string into list by spaces
    
    # Initialize the count for differences
    differenceCount = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert string elements to integers
        a = int(splitInput1[index])  # Convert first list element to integer
        b = int(splitInput2[index])  # Convert second list element to integer
        
        # Check if the elements are different
        if a != b:
            differenceCount += 1  # Increment count if they are different
    
    # Output result based on the number of differences
    if differenceCount < 3:
        print("YES")  # Print YES if differences are less than 3
    else:
        print("NO")   # Print NO if differences are 3 or more

# Start the program execution
doMain()
