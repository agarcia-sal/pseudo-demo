def doMain():
    # Read two lines of input
    inputLine1 = input()
    inputLine2 = input()
    
    # Split the input lines into lists of strings
    list1 = inputLine1.split()  # split by spaces
    list2 = inputLine2.split()  # split by spaces

    # Initialize a counter for differences
    differenceCount = 0 

    # Compare elements of both lists
    for index in range(3):  # we assume both lists have at least 3 elements
        value1 = int(list1[index])  # convert to integer
        value2 = int(list2[index])  # convert to integer

        # Increment the difference count if values are not equal
        if value1 != value2:
            differenceCount += 1 

    # Check the number of differences and print result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program
if __name__ == "__main__":
    doMain()
