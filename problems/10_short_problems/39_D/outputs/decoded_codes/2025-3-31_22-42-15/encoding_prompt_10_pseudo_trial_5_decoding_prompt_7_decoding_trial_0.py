def doMain():
    # Step 1: Read two lines of input from the user
    t1 = input()  # Read first input string
    t2 = input()  # Read second input string

    # Step 2: Split the input strings into lists of strings
    tt1 = t1.split()  # Split first string by whitespace into a list
    tt2 = t2.split()  # Split second string by whitespace into a list

    # Step 3: Initialize the variable to count mismatches
    res = 0  # Counter for mismatches

    # Step 4: Loop through the first three elements of both lists
    for x in range(3):  # Iterate over indices 0, 1, 2
        # Convert string elements to integers
        a = int(tt1[x])  # Convert the x-th element of the first list to an integer
        b = int(tt2[x])  # Convert the x-th element of the second list to an integer

        # Step 5: Increment the mismatch counter if elements are not equal
        if a != b:  # Compare the two integers
            res += 1  # Increment mismatch counter

    # Step 6: Check the count of mismatches and print result
    if res < 3:  # If fewer than 3 mismatches
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO

# Entry Point
doMain()
