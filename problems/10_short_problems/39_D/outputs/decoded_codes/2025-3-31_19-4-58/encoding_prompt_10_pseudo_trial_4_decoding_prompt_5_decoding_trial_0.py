def do_main():
    # Read two lines of input from the user
    t1 = input()
    t2 = input()

    # Split the input strings into lists of substrings using space as a delimiter
    tt1 = t1.split()
    tt2 = t2.split()

    # Initialize the result counter for differences
    res = 0

    # Iterate over the first three elements of both lists
    for index in range(3):
        # Convert substrings to integers for comparison
        a = int(tt1[index])
        b = int(tt2[index])

        # Check if the values are different
        if a != b:
            res += 1  # Increment difference count

    # Determine if the number of differences is less than three
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main execution block
do_main()
