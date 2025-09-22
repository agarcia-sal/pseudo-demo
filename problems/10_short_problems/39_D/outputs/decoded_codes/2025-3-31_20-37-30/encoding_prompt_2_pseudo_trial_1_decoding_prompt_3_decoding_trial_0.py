def doMain():
    # Read two strings from user input
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for differences
    differencesCount = 0

    # Iterate through the first three indices
    for index in range(3):  # As given, we check indices 0, 1, and 2
        # Convert values from the lists to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check for differences and update the counter
        if firstValue != secondValue:
            differencesCount += 1

    # Output based on the count of differences
    if differencesCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the function if the script is run directly
if __name__ == "__main__":
    doMain()
