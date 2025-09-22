def doMain():
    # Initialize variables
    t1 = ""
    t2 = ""
    tt1 = []
    tt2 = []
    res = 0

    # Read two lines of input from the user
    t1 = input()
    t2 = input()

    # Split the input strings into lists of substrings
    tt1 = t1.split()
    tt2 = t2.split()

    # Iterate over the first three elements of both lists
    for index in range(3):
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
doMain()
