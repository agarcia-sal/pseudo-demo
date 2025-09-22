def doMain():
    # Receive input for the first and second sets of numbers
    firstSet = input()
    secondSet = input()

    # Split the input strings into lists of numbers
    listFirst = firstSet.split()
    listSecond = secondSet.split()

    # Initialize a counter for the differing positions
    differenceCount = 0

    # Compare the numbers in the two lists
    for i in range(3):  # Since we expect exactly three numbers
        # Convert the current elements from the lists to integers
        numberFromFirst = int(listFirst[i])
        numberFromSecond = int(listSecond[i])

        # Check if the numbers differ
        if numberFromFirst != numberFromSecond:
            differenceCount += 1

    # Determine whether the differences are fewer than three
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the function if the script is run directly
if __name__ == "__main__":
    doMain()
