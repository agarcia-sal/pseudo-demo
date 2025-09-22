def doMain():
    # Read two strings from user input
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a variable to count differences
    differencesCount = 0

    # Loop over the index from 0 to 2 (inclusive)
    for index in range(3):
        # Convert the current index values to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # If the values differ, increment the count
        if firstValue != secondValue:
            differencesCount += 1

    # After checking all pairs, output based on the differences count
    if differencesCount < 3:
        print("YES")
    else:
        print("NO")

# Call the doMain function if the script is executed directly
if __name__ == "__main__":
    doMain()
