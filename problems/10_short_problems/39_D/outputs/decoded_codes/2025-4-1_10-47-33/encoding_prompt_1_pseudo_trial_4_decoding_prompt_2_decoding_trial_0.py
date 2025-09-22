def main():
    # Prompt user for input and store in variables
    firstInput = input()
    secondInput = input()
    
    # Split inputs into lists
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    differenceCount = 0

    # Compare the elements of both lists
    for index in range(3):
        # Convert string elements to integers for comparison
        valueFromFirstList = int(firstList[index])
        valueFromSecondList = int(secondList[index])

        # Check if the values are different
        if valueFromFirstList != valueFromSecondList:
            differenceCount += 1

    # Evaluate how many differences were found
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
