def do_main():
    # Step 1: Read inputs
    t1 = input()  # Read first input from user
    t2 = input()  # Read second input from user

    # Step 2: Split input strings into lists
    tt1 = t1.split()  # Split string t1 into a list of strings
    tt2 = t2.split()  # Split string t2 into a list of strings

    # Step 3: Initialize a counter for differences
    difference_count = 0 

    # Step 4: Loop through the first three elements of both lists
    for x in range(3):  # Loop from 0 to 2
        # Step 5: Convert string elements to integers
        a = int(tt1[x])  # Convert tt1 element to integer
        b = int(tt2[x])  # Convert tt2 element to integer

        # Step 6: Check for inequality
        if a != b:  # If a is not equal to b
            difference_count += 1  # Increment difference count

    # Step 7: Determine the output based on the count of differences
    if difference_count < 3:  # If differences are less than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Step 8: Execute the main function
do_main()
