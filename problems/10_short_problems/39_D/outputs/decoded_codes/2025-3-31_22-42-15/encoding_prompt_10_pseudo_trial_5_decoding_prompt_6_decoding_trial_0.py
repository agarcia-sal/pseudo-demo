def do_main():
    # Step 1: Read two lines of input from the user
    t1 = input()  # First line of input
    t2 = input()  # Second line of input

    # Step 2: Split the input strings into lists of strings
    tt1 = t1.split()  # List of string elements from first input
    tt2 = t2.split()  # List of string elements from second input

    # Step 3: Initialize the variable to count mismatches
    mismatch_count = 0  # Counter for mismatches 

    # Step 4: Loop through the first three elements of both lists
    for x in range(3):  # Iterate from 0 to 2
        # Convert string elements to integers
        a = int(tt1[x])  # First list element as integer
        b = int(tt2[x])  # Second list element as integer

        # Step 5: Increment the mismatch counter if elements are not equal
        if a != b:  # Check for mismatch
            mismatch_count += 1  # Increment counter

    # Step 6: Check the count of mismatches and print result
    if mismatch_count < 3:  # If mismatches are less than 3
        print("YES")  # Print "YES"
    else:
        print("NO")  # Print "NO"

# Entry Point
do_main()  # Call the main function
