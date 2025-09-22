def doMain():
    # Read two strings from user input
    firstInput = input()
    secondInput = input()
    
    # Split the inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for differences
    differencesCount = 0

    # Compare the corresponding values in the two lists
    for index in range(3):
        # Convert the values to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Increment the difference count if values are not equal
        if firstValue != secondValue:
            differencesCount += 1

    # Output "YES" if the number of differences is less than 3, otherwise "NO"
    if differencesCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the program only if it is run directly
if __name__ == "__main__":
    doMain()
