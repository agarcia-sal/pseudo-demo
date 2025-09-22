def doMain():
    # Step 1: Read inputs
    t1 = input()
    t2 = input()

    # Step 2: Split input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()

    # Step 3: Initialize a counter for differences
    res = 0 

    # Step 4: Loop through the first three elements of both lists
    for x in range(3):
        # Step 5: Convert string elements to integers
        a = int(tt1[x])
        b = int(tt2[x])

        # Step 6: Check for inequality
        if a != b:
            res += 1  # INCREMENT res by 1 if values are different

    # Step 7: Determine the output based on the count of differences
    if res < 3:
        print("YES")
    else:
        print("NO")

# Step 8: Execute the main function
doMain()
