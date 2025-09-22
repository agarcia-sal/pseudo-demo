def do_main():
    # Step 1: Read two lines of input and store them in variables
    t1 = input()  # First input string
    t2 = input()  # Second input string

    # Step 2: Split the input strings into lists of substrings
    tt1 = t1.split()  # Split into a list called tt1
    tt2 = t2.split()  # Split into a list called tt2

    # Step 3: Initialize a variable to count differences
    difference_count = 0 

    # Step 4: Compare elements of the two lists
    for index in range(3):  # Loop through the first three indices
        # Convert the substring to an integer for comparison
        a = int(tt1[index])  # Integer value of tt1[index]
        b = int(tt2[index])  # Integer value of tt2[index]

        # Step 5: Increment the count if the numbers are not equal
        if a != b:  # Check if a is not equal to b
            difference_count += 1  # Increment the difference count

    # Step 6: Determine output based on the number of differences
    if difference_count < 3:  # Check if differences are less than 3
        print("YES")  # Print YES
    else:
        print("NO")  # Print NO

# Step 7: Main execution block
if __name__ == "__main__":  # Check if the script is run as the main program
    do_main()  # Call the do_main function
