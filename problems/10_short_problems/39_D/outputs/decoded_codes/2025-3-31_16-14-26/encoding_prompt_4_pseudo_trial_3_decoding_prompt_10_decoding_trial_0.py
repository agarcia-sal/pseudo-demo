def do_main():
    # Read two lines of input
    input_line1 = input()
    input_line2 = input()

    # Split the input lines into lists of strings
    list1 = input_line1.split()  # Split by space
    list2 = input_line2.split()  # Split by space

    # Initialize a counter for differences
    difference_count = 0 

    # Compare elements of both lists
    for index in range(3):  # We expect exactly 3 elements to compare
        value1 = int(list1[index])  # Convert string to integer
        value2 = int(list2[index])  # Convert string to integer

        # Increment the difference count if values are not equal
        if value1 != value2:
            difference_count += 1 

    # Check the number of differences and print result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")


# It is good practice to include this check
if __name__ == "__main__":
    do_main()


# Test Case 1
# Input:
# 1 2 3
# 1 2 4
# Output: YES

# Test Case 2
# Input:
# 5 10 15
# 5 10 15
# Output: YES

# Test Case 3
# Input:
# 5 5 5
# 1 2 3
# Output: NO
