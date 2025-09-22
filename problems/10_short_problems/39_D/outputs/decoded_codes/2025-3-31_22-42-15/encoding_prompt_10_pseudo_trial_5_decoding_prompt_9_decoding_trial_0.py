def doMain():
    # Step 1: Read two lines of input from the user
    t1 = input()
    t2 = input()

    # Step 2: Split the input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()

    # Step 3: Initialize the variable to count mismatches
    res = 0 

    # Step 4: Loop through the first three elements of both lists
    for x in range(3):
        # Convert string elements to integers
        a = int(tt1[x])
        b = int(tt2[x])

        # Step 5: Increment the mismatch counter if elements are not equal
        if a != b:
            res += 1

    # Step 6: Check the count of mismatches and print result
    if res < 3:
        print("YES")
    else:
        print("NO")

# Entry Point
doMain()
