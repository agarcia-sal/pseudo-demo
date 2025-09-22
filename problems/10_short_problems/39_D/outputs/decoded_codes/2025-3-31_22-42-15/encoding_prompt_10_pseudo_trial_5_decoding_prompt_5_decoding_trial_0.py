def do_main():
    # Step 1: Read two lines of input from the user
    t1 = input()  # First input string
    t2 = input()  # Second input string

    # Step 2: Split the input strings into lists of strings
    tt1 = t1.split()  # List of strings from the first input
    tt2 = t2.split()  # List of strings from the second input

    # Step 3: Initialize the variable to count mismatches
    mismatch_count = 0 

    # Step 4: Loop through the first three elements of both lists
    for x in range(3):
        # Convert string elements to integers
        a = int(tt1[x])  # Convert to integer from first list
        b = int(tt2[x])  # Convert to integer from second list

        # Step 5: Increment the mismatch counter if elements are not equal
        if a != b:
            mismatch_count += 1

    # Step 6: Check the count of mismatches and print result
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Entry Point
do_main()
