def doMain():
    # Declare variables for user input
    input1 = input()  # Read first line of input
    input2 = input()  # Read second line of input
    
    # Split the inputs into lists based on spaces
    split_input1 = input1.split()
    split_input2 = input2.split()
    
    # Initialize difference count
    difference_count = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert string elements to integers
        a = int(split_input1[index])
        b = int(split_input2[index])
        
        # Check if the elements are different
        if a != b:
            difference_count += 1  # Increment difference count
    
    # Output result based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")
        
# Start the program execution
doMain()
