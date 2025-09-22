def main():
    # Read two lines of input representing two sets of values
    firstSet = input()
    secondSet = input()

    # Split the input strings into lists of values
    list1 = firstSet.split()
    list2 = secondSet.split()

    # Initialize a counter for differences
    differenceCount = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current element from each list to an integer
        value1 = int(list1[index])
        value2 = int(list2[index])
        
        # Check if the two values are different
        if value1 != value2:
            # Increment the difference counter
            differenceCount += 1

    # Check the number of differences
    if differenceCount < 3:
        # If fewer than 3 differences, print "YES"
        print("YES")
    else:
        # Otherwise, print "NO"
        print("NO")

# Execute the main function if the script is run as the main program
if __name__ == "__main__":
    main()
