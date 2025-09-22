def doMain():
    # Initialize input variables
    input1 = input()  # Read first line of input
    input2 = input()  # Read second line of input
    
    # Split the inputs into lists based on spaces
    splitInput1 = input1.split()  # Split first input into a list
    splitInput2 = input2.split()  # Split second input into a list
    
    # Initialize a counter for the differences
    differenceCount = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):  # Iterate from 0 to 2 inclusive
        # Convert string elements to integers
        a = int(splitInput1[index])  # Convert element from first input
        b = int(splitInput2[index])  # Convert element from second input
        
        # Check if the elements are different
        if a != b:  # If the elements are not equal
            differenceCount += 1  # Increment the difference counter
    
    # Output result based on the number of differences
    if differenceCount < 3:  # If fewer than three differences found
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Start the program execution
doMain()  # Call the main function to run the program
