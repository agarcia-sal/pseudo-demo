def doMain():
    # Step 1: Read input strings
    t1 = input()  # Read first input
    t2 = input()  # Read second input

    # Step 2: Split input strings into lists of strings
    tt1 = t1.split()  # Split t1 by whitespace
    tt2 = t2.split()  # Split t2 by whitespace

    # Step 3: Initialize a counter for differences
    difference_count = 0

    # Step 4: Loop through the elements of the lists
    for index in range(3):  # Assuming inputs have at least 3 elements
        # Convert string elements to integers
        a = int(tt1[index])  # Convert element from tt1
        b = int(tt2[index])  # Convert element from tt2

        # Count the number of differences
        if a != b:
            difference_count += 1

    # Step 5: Check the number of differences and output result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# This will call the function when the script is executed
doMain()
