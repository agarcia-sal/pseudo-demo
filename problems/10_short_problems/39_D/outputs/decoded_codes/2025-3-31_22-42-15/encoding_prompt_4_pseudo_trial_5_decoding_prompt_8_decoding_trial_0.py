def doMain():
    # Read input strings
    t1 = input()
    t2 = input()

    # Split the input strings into lists of values
    tt1 = t1.split()
    tt2 = t2.split()

    # Initialize a variable to count differences
    differenceCount = 0

    # Iterate over the first three elements of both lists
    for index in range(3):
        valueA = int(tt1[index])
        valueB = int(tt2[index])

        # Check if the values are different
        if valueA != valueB:
            differenceCount += 1

    # Check the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main execution
doMain()
