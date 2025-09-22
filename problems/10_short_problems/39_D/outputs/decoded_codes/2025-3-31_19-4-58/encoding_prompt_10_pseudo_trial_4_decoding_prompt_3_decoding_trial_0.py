def doMain():
    # Initialize variables to store user inputs and the count of differences
    t1 = input()
    t2 = input()
    tt1 = t1.split()  # Split input string t1 by space
    tt2 = t2.split()  # Split input string t2 by space
    res = 0  # Initialize the result counter for differences

    # Iterate over the first three elements of both input lists
    for index in range(3):
        a = int(tt1[index])  # Convert string to integer from the first list
        b = int(tt2[index])  # Convert string to integer from the second list

        # Check if the values from both lists are different
        if a != b:
            res += 1  # Increment the difference counter

    # Determine if the number of differences is less than three
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main execution block
doMain()
