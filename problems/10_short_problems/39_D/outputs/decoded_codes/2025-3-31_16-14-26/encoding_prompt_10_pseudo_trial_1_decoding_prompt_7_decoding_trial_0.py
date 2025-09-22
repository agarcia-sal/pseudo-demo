def doMain():
    # Step 1: Input values
    t1 = input()  # Read first line of input
    t2 = input()  # Read second line of input

    # Step 2: Split input strings into lists
    tt1 = t1.split()  # Split the first input by whitespace
    tt2 = t2.split()  # Split the second input by whitespace

    # Step 3: Initialize result counter
    res = 0  # Counter for differing values

    # Step 4: Compare elements in the lists
    for x in range(3):  # Loop to compare the first three elements
        a = int(tt1[x])  # Convert the x-th element from the first list to an integer
        b = int(tt2[x])  # Convert the x-th element from the second list to an integer

        # Step 5: Increment result if values differ
        if a != b:  # Check if the values are not equal
            res += 1  # Increment the count of differing values

    # Step 6: Print result based on comparison count
    if res < 3:  # If fewer than 3 elements differ
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Step 7: Start execution
doMain()


       1 2 3
       1 2 4
       

       5 10 15
       5 10 15
       

       1 1 1
       2 2 2
       

       3 4 5
       3 5 6
       