def do_main():
    # Step 1: Read two lines of input
    t1 = input()  # First line input
    t2 = input()  # Second line input

    # Step 2: Split the input strings into lists of strings
    tt1 = t1.split()  # Split first input by spaces
    tt2 = t2.split()  # Split second input by spaces

    # Step 3: Initialize a count for differences
    res = 0  # Counter for differences

    # Step 4: Compare corresponding elements in the two lists
    for x in range(3):  # Loop through the indices 0 to 2
        # Step 4a: Convert string elements to integer
        a = int(tt1[x])  # Convert to integer from the first list
        b = int(tt2[x])  # Convert to integer from the second list

        # Step 4b: Check for differences
        if a != b:  # Compare the two integers
            res += 1  # Increment the difference counter if not equal

    # Step 5: Check the count of differences and output the result
    if res < 3:  # Check if differences are less than 3
        print("YES")  # Output YES if differences are less than 3
    else:
        print("NO")  # Output NO if differences are 3 or more

# Main Execution Block
do_main()  # Call the main function to execute the logic


     1 2 3
     1 2 3
     

     1 2 3
     1 2 4
     

     1 2 3
     4 2 5
     

     1 2 3
     4 5 6
     

     -1 -2 -3
     -1 -3 -2
     