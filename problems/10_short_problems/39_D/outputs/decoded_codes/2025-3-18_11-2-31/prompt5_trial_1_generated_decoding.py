def runComparison():
    # Accept input from the user for the first set of numbers
    firstSet = input()
    # Accept input from the user for the second set of numbers
    secondSet = input()

    # Split the input into separate numbers and store in lists
    firstNumbers = firstSet.split()
    secondNumbers = secondSet.split()
    
    # Initialize the counter for differences
    differenceCount = 0

    # Compare each number at the same index in both lists
    for index in range(3):
        # Convert the current numbers to integers
        numberFromFirstSet = int(firstNumbers[index])
        numberFromSecondSet = int(secondNumbers[index])
        
        # Check if the numbers are different
        if numberFromFirstSet != numberFromSecondSet:
            # Increment the difference count by 1 for each difference found
            differenceCount += 1

    # Evaluate the number of differences
    if differenceCount < 3:
        print("YES")  # Fewer than 3 numbers differ
    else:
        print("NO")   # At least 3 numbers differ

# Run the main function if this script is executed directly
if __name__ == "__main__":
    runComparison()
