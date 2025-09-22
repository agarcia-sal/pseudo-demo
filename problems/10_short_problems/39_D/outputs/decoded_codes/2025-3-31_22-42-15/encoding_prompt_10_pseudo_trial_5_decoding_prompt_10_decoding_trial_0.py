def do_main():
    # Step 1: Read two lines of input from the user
    input1 = input()
    input2 = input()

    # Step 2: Split the input strings into lists of strings
    values1 = input1.split()
    values2 = input2.split()

    # Step 3: Initialize the variable to count mismatches
    mismatch_count = 0 

    # Step 4: Loop through the first three elements of both lists
    for i in range(3):
        # Convert string elements to integers
        a = int(values1[i])
        b = int(values2[i])

        # Step 5: Increment the mismatch counter if elements are not equal
        if a != b:
            mismatch_count += 1

    # Step 6: Check the count of mismatches and print result
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Entry Point
do_main()


    Input:
    1 2 3
    1 2 3
    Output: YES
    

    Input:
    1 2 3
    4 2 3
    Output: YES
    

    Input:
    1 2 3
    4 5 6
    Output: NO
    