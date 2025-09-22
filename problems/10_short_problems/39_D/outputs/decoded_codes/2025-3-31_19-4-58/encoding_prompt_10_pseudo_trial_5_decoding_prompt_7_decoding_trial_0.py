def doMain():
    # Step 1: Read input values from the user
    t1 = input()  # First string input
    t2 = input()  # Second string input

    # Step 2: Split the input strings into lists of strings
    tt1 = t1.split()  # Split the first input string at spaces
    tt2 = t2.split()  # Split the second input string at spaces

    # Step 3: Initialize result counter
    res = 0  # Counter for differences

    # Step 4: Iterate over the first three elements in the lists
    for x in range(3):  # Loop through the first three indices (0 to 2)
        a = int(tt1[x])  # Convert string from the first list to integer
        b = int(tt2[x])  # Convert string from the second list to integer

        # Step 5: Compare both integers
        if a != b:  # Check if the two integers are not equal
            res += 1  # Increment the result counter by 1 if they are different

    # Step 6: Determine and print the result based on comparisons
    if res < 3:  # If less than 3 differences
        print("YES")  # Print "YES"
    else:
        print("NO")  # Print "NO"

# Step 7: Main entry point of the program
if __name__ == "__main__":
    doMain()  # Call the main function
