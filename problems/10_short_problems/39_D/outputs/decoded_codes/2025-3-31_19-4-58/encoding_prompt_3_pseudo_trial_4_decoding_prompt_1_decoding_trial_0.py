def main():
    # Read two lines of input representing two sequences of numbers
    firstSequence = input()
    secondSequence = input()

    # Split the input strings into lists of strings
    firstList = firstSequence.split()
    secondList = secondSequence.split()

    # Initialize a variable to count the number of differences
    differenceCount = 0 

    # Iterate over the first three elements of both lists
    for index in range(3):
        # Convert the current elements from strings to integers
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])

        # Check if the two numbers are different
        if firstNumber != secondNumber:
            # Increment the difference count
            differenceCount += 1

    # Determine whether fewer than 3 differences exist
    if differenceCount < 3:
        # If yes, print "YES"
        print("YES")
    else:
        # Otherwise, print "NO"
        print("NO")

# Start the program
main()
