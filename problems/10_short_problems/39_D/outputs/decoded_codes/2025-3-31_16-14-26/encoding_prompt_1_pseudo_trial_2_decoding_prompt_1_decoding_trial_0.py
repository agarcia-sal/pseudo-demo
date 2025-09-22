def main():
    # Step 1: Get input
    firstInput = input()
    secondInput = input()

    # Step 2: Split the inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter to track differences
    differenceCount = 0

    # Step 3: Compare corresponding elements of the two lists
    for index in range(3):
        # Convert string elements to integers
        valueFromFirstList = int(firstList[index])
        valueFromSecondList = int(secondList[index])
        
        # Check if the values are different
        if valueFromFirstList != valueFromSecondList:
            differenceCount += 1

    # Step 4: Check the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Invoke the main function when running the program
main()
