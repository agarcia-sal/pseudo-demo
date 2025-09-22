def do_main():
    # Step 1: Input values
    t1 = input()  # Read input from user
    t2 = input()  # Read input from user

    # Step 2: Split input strings into lists
    tt1 = t1.split()  # Split t1 by whitespace
    tt2 = t2.split()  # Split t2 by whitespace
    
    # Step 3: Initialize result counter
    res = 0  # Counter for differences

    # Step 4: Compare elements in the lists
    for x in range(3):  # Loop through first three elements
        a = int(tt1[x])  # Convert string to integer
        b = int(tt2[x])  # Convert string to integer

        # Step 5: Increment result if values differ
        if a != b:
            res += 1  # Increase counter if values are not equal

    # Step 6: Print result based on comparison count
    if res < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Start execution
do_main()
