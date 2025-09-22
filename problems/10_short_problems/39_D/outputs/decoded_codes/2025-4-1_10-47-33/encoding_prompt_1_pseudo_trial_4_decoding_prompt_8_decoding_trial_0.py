def main():
    firstInput = input()
    secondInput = input()
    
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    differenceCount = 0

    # Compare the elements of both lists
    for index in range(3):
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
