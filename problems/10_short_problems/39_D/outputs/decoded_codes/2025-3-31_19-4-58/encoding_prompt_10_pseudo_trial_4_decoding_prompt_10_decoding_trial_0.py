def do_main():
    """
    Main function to compare two input strings of integers.
    It determines how many numbers differ between the two inputs and prints
    'YES' if fewer than three numbers are different, otherwise 'NO'.
    """
    # Read two lines of input from the user
    t1 = input()
    t2 = input()

    # Split the input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()

    # Initialize the result counter
    res = 0

    # Only process the first three elements from both lists
    for index in range(3):
        # Convert the string values to integers
        a = int(tt1[index])
        b = int(tt2[index])

        # Check if the values are different
        if a != b:
            res += 1

    # Determine if the number of differences is less than three
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main execution block
do_main()
