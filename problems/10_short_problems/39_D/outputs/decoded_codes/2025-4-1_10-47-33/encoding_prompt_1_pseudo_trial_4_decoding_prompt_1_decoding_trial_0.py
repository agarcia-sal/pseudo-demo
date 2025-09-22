def main():
    # Prompt user for input and store in variable firstInput
    firstInput = input()
    
    # Prompt user for input and store in variable secondInput
    secondInput = input()
    
    # Split firstInput into a list called firstList
    firstList = firstInput.split()
    
    # Split secondInput into a list called secondList
    secondList = secondInput.split()
    
    # Set differenceCount to 0
    differenceCount = 0

    # Compare the elements of both lists
    for index in range(3):  # Loop from 0 to 2
        # Convert string elements to integers for comparison
        valueFromFirstList = int(firstList[index])
        valueFromSecondList = int(secondList[index])

        # Check if the values are different
        if valueFromFirstList != valueFromSecondList:
            # Increment differenceCount by 1
            differenceCount += 1

    # Evaluate how many differences were found
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
