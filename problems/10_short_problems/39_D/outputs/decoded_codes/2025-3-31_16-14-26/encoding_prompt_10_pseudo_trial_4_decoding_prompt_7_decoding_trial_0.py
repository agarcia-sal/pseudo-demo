def doMain():
    # Step 1: Read input
    t1 = input()  # Read a line of input
    t2 = input()  # Read a second line of input

    # Step 2: Split the inputs into lists
    tt1 = t1.split()  # Split the first input into a list of strings
    tt2 = t2.split()  # Split the second input into a list of strings

    # Step 3: Initialize a counter to track differences
    res = 0  # Initialize the result counter to 0

    # Step 4: Compare elements in both lists
    for x in range(3):  # Loop over the first three elements in the lists
        # Convert string elements to integers
        a = int(tt1[x])  # Convert the x-th element of tt1 to integer
        b = int(tt2[x])  # Convert the x-th element of tt2 to integer
        
        # If the elements are not equal, increment the counter
        if a != b:  # Check if the integers are not equal
            res += 1  # Increment the counter by 1 for each difference

    # Step 5: Determine and output the result based on the counter
    if res < 3:  # Check if the count of differences is less than 3
        print("YES")  # Print "YES" if there are less than 3 differences
    else:
        print("NO")  # Print "NO" otherwise

# Program Execution Start
doMain()  # Call the main function to execute the program


     1 2 3
     1 2 3
     

     1 2 3
     3 2 1
     

     1 2 3
     4 5 6
     

     1 2 3
     3 2 3
     

     1 2 3
     1 2 4
     