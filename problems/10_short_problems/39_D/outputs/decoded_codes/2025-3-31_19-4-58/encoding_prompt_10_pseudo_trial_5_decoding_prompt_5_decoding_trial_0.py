def do_main():
    # Step 1: Read input values from the user
    t1 = input()
    t2 = input()

    # Step 2: Split the input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()

    # Step 3: Initialize result counter
    res = 0

    # Step 4: Iterate over the first three elements in the lists
    for x in range(3):
        a = int(tt1[x])  # Convert to integer
        b = int(tt2[x])  # Convert to integer

        # Step 5: Compare both integers
        if a != b:
            res += 1  # Increment if values are not equal

    # Step 6: Determine and print the result based on comparisons
    if res < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Main entry point of the program
if __name__ == "__main__":
    do_main()
