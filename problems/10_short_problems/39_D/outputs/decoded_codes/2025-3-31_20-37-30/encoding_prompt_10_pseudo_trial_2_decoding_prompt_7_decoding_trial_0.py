def doMain():
    # Obtain two strings from user input
    string1 = input()
    string2 = input()

    # Split the strings into lists of elements
    list1 = string1.split()
    list2 = string2.split()

    # Initialize a variable to count the differences
    differenceCount = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the elements to integers
        valueA = int(list1[index])
        valueB = int(list2[index])
        
        # Check if the values are different
        if valueA != valueB:
            # Increment the difference count
            differenceCount += 1

    # Determine if fewer than 3 differences are found
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute main function if this is the program entry point
if __name__ == "__main__":
    doMain()
