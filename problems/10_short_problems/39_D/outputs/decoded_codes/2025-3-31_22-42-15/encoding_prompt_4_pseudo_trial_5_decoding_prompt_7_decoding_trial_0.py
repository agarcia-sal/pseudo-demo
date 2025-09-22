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
        valueA = int(tt1[index])  # Convert the string value to integer from first list
        valueB = int(tt2[index])  # Convert the string value to integer from second list

        # Check if the values are different
        if valueA != valueB:
            differenceCount += 1  # Increment difference count if values differ

    # Check the number of differences
    if differenceCount < 3:
        print("YES")  # Print "YES" if differences are less than 3
    else:
        print("NO")   # Print "NO" if differences are 3 or more

# Main execution
doMain()
