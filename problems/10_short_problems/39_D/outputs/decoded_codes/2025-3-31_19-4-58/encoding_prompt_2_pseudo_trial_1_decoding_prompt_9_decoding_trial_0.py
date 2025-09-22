def main():
    # Get Inputs
    firstInput = input()
    secondInput = input()
    
    # Split Inputs
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a Mismatch Counter
    mismatchCount = 0

    # Compare Values
    for index in range(3):
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        if firstValue != secondValue:
            mismatchCount += 1

    # Check Mismatch Count
    if mismatchCount < 3:
        print("YES")
    else:
        print("NO")

# Execute Main Function on Program Start
main()
