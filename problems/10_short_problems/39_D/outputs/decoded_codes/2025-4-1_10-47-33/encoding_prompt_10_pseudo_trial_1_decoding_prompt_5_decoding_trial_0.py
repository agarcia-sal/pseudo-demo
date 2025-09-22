def do_main():
    # Step 1: Read input strings
    t1 = input()  # First input string
    t2 = input()  # Second input string

    # Step 2: Split input strings into lists
    tt1 = t1.split()  # List of numbers from the first string
    tt2 = t2.split()  # List of numbers from the second string

    # Step 3: Initialize a variable to count differences
    difference_count = 0

    # Step 4: Loop through the first three elements of the lists
    for x in range(3):  # Loop from 0 to 2
        # Step 5: Convert string elements to integers
        a = int(tt1[x])  # Convert the x-th element of tt1 to integer
        b = int(tt2[x])  # Convert the x-th element of tt2 to integer
        
        # Step 6: Compare the values and increment difference count if not equal
        if a != b:  # Compare the two integers
            difference_count += 1  # Increment difference count if they are not equal

    # Step 7: Check the number of differences and print the result
    if difference_count < 3:  # If less than 3 differences
        print("YES")  # Print "YES"
    else:
        print("NO")  # Otherwise, print "NO"

# Step 8: Execute the main function when the script runs
do_main()
