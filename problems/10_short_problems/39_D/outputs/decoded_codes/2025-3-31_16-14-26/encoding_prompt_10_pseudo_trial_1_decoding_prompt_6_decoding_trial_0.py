def do_main():
    # Step 1: Input values
    t1 = input()  # Read input from user
    t2 = input()  # Read input from user

    # Step 2: Split input strings into lists
    tt1 = t1.split()  # Split t1 into a list of strings
    tt2 = t2.split()  # Split t2 into a list of strings

    # Step 3: Initialize the result counter
    result_counter = 0  # Count how many values differ

    # Step 4: Compare elements in the lists
    for x in range(3):  # Loop over the first three elements
        a = int(tt1[x])  # Convert tt1[x] to an integer
        b = int(tt2[x])  # Convert tt2[x] to an integer

        # Step 5: Increment result counter if values differ
        if a != b:  # Check if values are not equal
            result_counter += 1  # Increment counter

    # Step 6: Print result based on comparison count
    if result_counter < 3:
        print("YES")  # Print YES if fewer than 3 values differ
    else:
        print("NO")  # Print NO if 3 or more values differ

# Step 7: Start execution
do_main()
