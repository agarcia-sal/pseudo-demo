def doMain():
    # Receive inputs for the two sets of numbers from the user
    firstSet = input()
    secondSet = input()

    # Split the input strings into lists of individual numbers
    listFirst = firstSet.split()
    listSecond = secondSet.split()

    # Initialize the difference counter
    differenceCount = 0

    # Compare the numbers in both lists
    for index in range(3):  # Loop through the indices 0 to 2
        # Convert the numbers to integers
        numberFromFirst = int(listFirst[index])
        numberFromSecond = int(listSecond[index])

        # Check for differences
        if numberFromFirst != numberFromSecond:
            differenceCount += 1

    # Check the difference count and output accordingly
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the function directly
if __name__ == "__main__":
    doMain()
