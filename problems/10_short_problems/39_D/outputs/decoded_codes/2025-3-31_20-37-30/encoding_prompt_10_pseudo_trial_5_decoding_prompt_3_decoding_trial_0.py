def do_main():
    # Step 1: Read two lines of input
    t1 = input()
    t2 = input()

    # Step 2: Split the input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Step 3: Initialize a count for differences
    res = 0

    # Step 4: Compare corresponding elements in the two lists
    for x in range(3):  # Assumes that there are exactly three elements to compare
        # Step 4a: Convert string elements to integer
        a = int(tt1[x])
        b = int(tt2[x])

        # Step 4b: Check for differences
        if a != b:
            res += 1  # Increment count if the values are different

    # Step 5: Check the count of differences and output the result
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main Execution Block
do_main()
