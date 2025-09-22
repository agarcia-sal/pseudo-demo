def do_main():
    # Step 1: Input values
    t1 = input()  # Read input from user
    t2 = input()  # Read input from user

    # Step 2: Split input strings into lists
    tt1 = t1.split()  # Split t1 by whitespace into a list of strings
    tt2 = t2.split()  # Split t2 by whitespace into a list of strings

    # Step 3: Initialize result counter
    res = 0  # Counter for differing elements

    # Step 4: Compare elements in the lists
    for x in range(3):  # Loop through indices 0 to 2
        a = int(tt1[x])  # Convert string to integer
        b = int(tt2[x])  # Convert string to integer

        # Step 5: Increment result if values differ
        if a != b:  # If values are not equal
            res += 1  # Increment the counter

    # Step 6: Print result based on comparison count
    if res < 3:  # If fewer than 3 values differ
        print("YES")  # Print YES
    else:
        print("NO")  # Print NO

# Step 7: Start execution
do_main()
