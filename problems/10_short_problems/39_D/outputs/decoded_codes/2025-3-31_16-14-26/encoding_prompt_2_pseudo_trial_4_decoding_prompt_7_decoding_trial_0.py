def main():
    # Input Phase: Collect sequences from user
    firstSequence = input()  # Prompt user to enter the first sequence
    secondSequence = input()  # Prompt user to enter the second sequence

    # Process Input: Split sequences into lists
    firstList = firstSequence.split()  # Split firstSequence into a list of strings
    secondList = secondSequence.split()  # Split secondSequence into a list of strings

    # Initialize Difference Counter
    differenceCount = 0  # Counter to track differences between two sequences

    # Comparison Loop: Compare numbers at each position
    for i in range(3):  # There are three numbers to compare
        numberFromFirst = int(firstList[i])  # Convert first number to integer
        numberFromSecond = int(secondList[i])  # Convert second number to integer
        if numberFromFirst != numberFromSecond:  # Check if they are different
            differenceCount += 1  # Increment counter for each difference

    # Decision-making: Output result based on difference count
    if differenceCount < 3:  # If differences are less than 3
        print("YES")  # Indicate they differ in less than three positions
    else:
        print("NO")  # Indicate they differ in three or more positions

# The main function will execute when the script runs
if __name__ == "__main__":
    main()
