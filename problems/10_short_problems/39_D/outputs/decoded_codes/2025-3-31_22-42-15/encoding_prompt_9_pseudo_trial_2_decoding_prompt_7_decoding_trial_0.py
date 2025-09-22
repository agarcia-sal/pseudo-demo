def doMain():
    # Receive Input
    firstSet = input()  # Get first set of three numbers
    secondSet = input()  # Get second set of three numbers

    # Split the Input into Lists
    listFirst = firstSet.split()  # Split input into list of numbers
    listSecond = secondSet.split()  # Split second input into list of numbers

    # Initialize Difference Counter
    differenceCount = 0  # Counter for differing numbers

    # Compare the Numbers
    for index in range(3):  # Loop over three positions
        numberFromFirst = int(listFirst[index])  # Convert to integer
        numberFromSecond = int(listSecond[index])  # Convert to integer
        if numberFromFirst != numberFromSecond:  # Check for difference
            differenceCount += 1  # Increment count if different

    # Check Differences
    if differenceCount < 3:  # Fewer than 3 differences
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO

# Execute the Function
if __name__ == "__main__":
    doMain()  # Call the doMain function if the script is executed
