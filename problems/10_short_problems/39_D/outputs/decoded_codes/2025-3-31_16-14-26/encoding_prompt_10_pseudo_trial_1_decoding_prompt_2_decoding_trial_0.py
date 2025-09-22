def doMain():
    # Step 1: Input values
    t1 = input()
    t2 = input()

    # Step 2: Split input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()

    # Step 3: Initialize result counter
    res = 0

    # Step 4: Compare elements in the lists
    for x in range(3):
        a = int(tt1[x])  # Convert string to integer
        b = int(tt2[x])  # Convert string to integer

        # Step 5: Increment result if values differ
        if a != b:
            res += 1

    # Step 6: Print result based on comparison count
    if res < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Start execution
doMain()
