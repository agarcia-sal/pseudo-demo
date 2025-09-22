def main():
    # Input Phase
    firstSequence = input()  # Enter the first sequence of three numbers
    secondSequence = input()  # Enter the second sequence of three numbers

    # Process Input
    firstList = firstSequence.split()  # Split the first sequence into a list
    secondList = secondSequence.split()  # Split the second sequence into a list

    # Initialize Difference Counter
    differenceCount = 0

    # Comparison Loop
    for i in range(3):  # Loop through the indices 0 to 2
        numberFromFirst = int(firstList[i])  # Convert to integer from first list
        numberFromSecond = int(secondList[i])  # Convert to integer from second list
        if numberFromFirst != numberFromSecond:  # Compare the numbers
            differenceCount += 1  # Increment the counter if they are different

    # Decision-making
    if differenceCount < 3:  # Check the difference count
        print("YES")  # Sequences differ in less than three positions
    else:
        print("NO")  # Sequences differ in three or more positions

# Execute the main function
main()
