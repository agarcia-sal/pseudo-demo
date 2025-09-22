def doMain():
    input1 = ""  # Declare input1 as string
    input2 = ""  # Declare input2 as string
    splitInput1 = []  # Declare splitInput1 as list
    splitInput2 = []  # Declare splitInput2 as list
    differenceCount = 0  # Declare differenceCount as integer initialized to 0
    
    # Read two lines of input
    input1 = input()  # Get user input
    input2 = input()  # Get user input
    
    # Split the inputs into lists
    splitInput1 = input1.split()  # Split input1 by spaces
    splitInput2 = input2.split()  # Split input2 by spaces

    # Loop through the first three elements of both lists
    for index in range(3):  # Loop from 0 to 2
        # Convert string elements to integers
        a = int(splitInput1[index])  # Convert splitInput1[index] to integer
        b = int(splitInput2[index])  # Convert splitInput2[index] to integer
        
        # Check if the elements are different
        if a != b:  # Check if a is not equal to b
            differenceCount += 1  # Increment differenceCount by 1

    # Output result based on the number of differences
    if differenceCount < 3:  # Check if differenceCount is less than 3
        print("YES")  # Print "YES"
    else:
        print("NO")  # Print "NO"

# Start the program execution
doMain()
