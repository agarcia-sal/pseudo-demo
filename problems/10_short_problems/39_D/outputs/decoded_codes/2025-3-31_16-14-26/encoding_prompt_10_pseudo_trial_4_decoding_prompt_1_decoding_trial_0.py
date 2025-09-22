def doMain():  
    # Step 1: Read input
    t1 = input()  # User input for the first line
    t2 = input()  # User input for the second line

    # Step 2: Split the inputs into lists
    tt1 = t1.split()  # Split the first input line into a list
    tt2 = t2.split()  # Split the second input line into a list

    # Step 3: Initialize a counter to track differences
    res = 0  # Initialize the counter

    # Step 4: Compare elements in both lists
    for x in range(3):  # Loop over the range 0 to 2 (inclusive)
        a = int(tt1[x])  # Convert string elements to integers
        b = int(tt2[x])  # Convert string elements to integers
        
        # If the elements are not equal, increment the counter
        if a != b:  # Check if elements are different
            res += 1  # Increment the counter

    # Step 5: Determine and output the result based on the counter
    if res < 3:  # Check if differences are less than 3
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO

# Program Execution Start
doMain()  # Call the main function
