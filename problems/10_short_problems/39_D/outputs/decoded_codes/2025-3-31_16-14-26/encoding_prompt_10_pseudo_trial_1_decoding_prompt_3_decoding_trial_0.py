def do_main():
    # Step 1: Input values
    t1 = input()  # Read first string input from the user
    t2 = input()  # Read second string input from the user

    # Step 2: Split input strings into lists
    tt1 = t1.split()  # Split the first input string by whitespace
    tt2 = t2.split()  # Split the second input string by whitespace

    # Step 3: Initialize result counter
    res = 0  # Counter for differing values

    # Step 4: Compare elements in the lists
    for x in range(3):  # Assuming each list contains at least three elements
        a = int(tt1[x])  # Convert the x-th element of tt1 to an integer
        b = int(tt2[x])  # Convert the x-th element of tt2 to an integer

        # Step 5: Increment result if values differ
        if a != b:  # Check if the elements are not equal
            res += 1  # Increment the counter

    # Step 6: Print result based on comparison count
    if res < 3:  # If fewer than three values differ
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Step 7: Start execution
do_main()
