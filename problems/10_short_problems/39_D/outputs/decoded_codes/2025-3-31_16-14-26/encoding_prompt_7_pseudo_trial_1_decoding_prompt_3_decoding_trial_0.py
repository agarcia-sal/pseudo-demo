def do_main():
    # Step 1: Read two lines of input and store them in variables
    t1 = input()  # First input string
    t2 = input()  # Second input string

    # Step 2: Split the input strings into lists of substrings
    tt1 = t1.split()  # Split first input into a list
    tt2 = t2.split()  # Split second input into a list

    # Step 3: Initialize a variable to count differences
    difference_count = 0

    # Step 4: Compare elements of the two lists
    for index in range(3):  # Loop over the first three elements
        a = int(tt1[index])  # Convert the substring to an integer
        b = int(tt2[index])  # Convert the substring to an integer

        # Step 5: Increment the count if the numbers are not equal
        if a != b:
            difference_count += 1  # Increment difference count

    # Step 6: Determine output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Main execution block
if __name__ == "__main__":
    do_main()
