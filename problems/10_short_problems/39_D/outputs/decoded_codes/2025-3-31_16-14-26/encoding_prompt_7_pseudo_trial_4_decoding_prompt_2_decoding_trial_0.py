def evaluateDifferencesBetweenInputs():
    # Read two input strings representing sequences of numbers
    firstSequence = input()
    secondSequence = input()

    # Split the input strings into lists of strings
    firstList = firstSequence.split()
    secondList = secondSequence.split()

    # Initialize a counter for differences
    differenceCount = 0

    # Loop through the first three elements of the lists
    for index in range(3):
        # Convert the string elements to integers
        numberFromFirstList = int(firstList[index])
        numberFromSecondList = int(secondList[index])

        # Check if the two numbers are not equal
        if numberFromFirstList != numberFromSecondList:
            # Increment the difference count
            differenceCount += 1

    # If the number of differences is less than 3, output "YES"
    if differenceCount < 3:
        print("YES")
    else:
        # Otherwise, output "NO"
        print("NO")

# Start execution of the program
if __name__ == "__main__":
    evaluateDifferencesBetweenInputs()
