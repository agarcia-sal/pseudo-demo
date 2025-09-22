def doMain():
    # Declare variables to hold user input
    t1 = ""
    t2 = ""
    res = 0  # Initialize the result counter

    # Read two lines of input from the user
    t1 = input()
    t2 = input()

    # Split the input strings into lists of substrings
    tt1 = t1.split()  # Splits t1 into a list
    tt2 = t2.split()  # Splits t2 into a list

    # Iterate over the first three elements of both lists
    for index in range(3):
        # Convert the string elements to integers
        a = int(tt1[index])
        b = int(tt2[index])

        # Check if the values are different
        if a != b:
            res += 1  # Increment the count of differences

    # Determine if the number of differences is less than three
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main execution block
doMain()
