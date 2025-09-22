def do_main():
    # Step 1: Read two lines of input and store them in variables
    t1 = input()  # First input string
    t2 = input()  # Second input string

    # Step 2: Split the input strings into lists of substrings
    tt1 = t1.split()  # List of substrings from the first input
    tt2 = t2.split()  # List of substrings from the second input

    # Step 3: Initialize a variable to count differences
    difference_count = 0 

    # Step 4: Compare elements of the two lists
    for index in range(3):  # Loop through indices 0 to 2
        # Convert the substring to an integer for comparison
        a = int(tt1[index])  # First number
        b = int(tt2[index])  # Second number

        # Step 5: Increment the count if the numbers are not equal
        if a != b:
            difference_count += 1  # Increment count of differences

    # Step 6: Determine output based on the number of differences
    if difference_count < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")   # 3 or more differences

# Step 7: Main execution block
if __name__ == "__main__":
    do_main()
