def doMain():
    # Receive Input
    firstSet = input()
    secondSet = input()

    # Split the Input
    listFirst = firstSet.split()
    listSecond = secondSet.split()

    # Initialize Difference Counter
    differenceCount = 0

    # Compare the Numbers
    for index in range(3):  # Loop through indices 0, 1, 2
        numberFromFirst = int(listFirst[index])  # Convert to integer
        numberFromSecond = int(listSecond[index])  # Convert to integer
        if numberFromFirst != numberFromSecond:  # Compare numbers
            differenceCount += 1  # Increment counter if different

    # Check Differences
    if differenceCount < 3:
        print("YES")  # Output YES if difference count is less than 3
    else:
        print("NO")  # Output NO otherwise

# Execute the Function
if __name__ == "__main__":
    doMain()
