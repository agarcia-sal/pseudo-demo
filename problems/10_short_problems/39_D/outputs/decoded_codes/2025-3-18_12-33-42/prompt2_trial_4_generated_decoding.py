def doMain():
    # Get input from the user
    firstInput = input()
    secondInput = input()
    
    # Split inputs into lists of words
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize difference count
    differenceCount = 0

    # Loop through the first three indexes (0 to 2)
    for index in range(3):
        # Convert to integers
        valueFromFirst = int(firstList[index])
        valueFromSecond = int(secondList[index])
        
        # Check for differences
        if valueFromFirst != valueFromSecond:
            differenceCount += 1

    # Conditional output based on difference count
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Check if the program is executed as the main program
if __name__ == "__main__":
    doMain()
