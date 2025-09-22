def doMain():
    # Initialize variables
    input1 = ""
    input2 = ""
    differenceCount = 0
    
    # Read two lines of input
    input1 = input()
    input2 = input()
    
    # Split the inputs into lists
    splitInput1 = input1.split()
    splitInput2 = input2.split()

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert string elements to integers
        a = int(splitInput1[index])
        b = int(splitInput2[index])
        
        # Check if the elements are different
        if a != b:
            differenceCount += 1

    # Output result based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution
doMain()
