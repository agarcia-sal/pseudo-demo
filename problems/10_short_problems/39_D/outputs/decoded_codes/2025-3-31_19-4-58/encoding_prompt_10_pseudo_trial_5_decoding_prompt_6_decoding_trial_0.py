def do_main():
    # Step 1: Read input values from the user
    t1 = input()
    t2 = input()

    # Step 2: Split the input strings into lists of strings
    tt1 = t1.split()  # Allows the user to input space-separated values
    tt2 = t2.split()  # This will create a list of input strings

    # Step 3: Initialize result counter
    res = 0  # Initialize the counter for discrepancies

    # Step 4: Iterate over the first three elements in the lists
    for x in range(3):
        a = int(tt1[x])  # Convert string to integer
        b = int(tt2[x])  # Convert string to integer

        # Step 5: Compare both integers
        if a != b:  # If the integers are not equal
            res += 1  # Increment the counter

    # Step 6: Determine and print the result based on comparisons
    if res < 3:  # If discrepancies are less than 3
        print("YES")  # Print "YES" if less than three numbers differ
    else:
        print("NO")  # Print "NO" if three or more numbers differ

# Step 7: Main entry point of the program
if __name__ == "__main__":
    do_main()
