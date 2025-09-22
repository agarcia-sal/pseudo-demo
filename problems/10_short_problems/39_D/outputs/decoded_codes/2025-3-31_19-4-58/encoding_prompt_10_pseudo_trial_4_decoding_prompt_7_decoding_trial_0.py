def doMain():
    # Initialize variables for input
    t1 = input()  # Get first line of input from the user
    t2 = input()  # Get second line of input from the user

    # Split the input strings into lists of substrings
    tt1 = t1.split()  # Split the first input string by spaces
    tt2 = t2.split()  # Split the second input string by spaces

    # Initialize result counter for differences
    res = 0

    # Iterate over the first three elements of both lists
    for index in range(3):
        a = int(tt1[index])  # Convert first list value to integer
        b = int(tt2[index])  # Convert second list value to integer

        # Check if the values are different
        if a != b:
            res += 1  # Increment the difference counter

    # Determine if the number of differences is less than three
    if res < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")  # 3 or more differences

# Main execution block
doMain()
