def doMain():
    # Step 1: Read input strings
    t1 = input()
    t2 = input()

    # Step 2: Split input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()

    # Step 3: Initialize a variable to count differences
    res = 0

    # Step 4: Loop through the first three elements of the lists
    for x in range(3):
        # Step 5: Convert string elements to integers
        a = int(tt1[x])
        b = int(tt2[x])
        
        # Step 6: Compare the values and increment difference count if not equal
        if a != b:
            res += 1

    # Step 7: Check the number of differences and print the result
    if res < 3:
        print("YES")
    else:
        print("NO")

# Step 8: Execute the main function when the script runs
doMain()
