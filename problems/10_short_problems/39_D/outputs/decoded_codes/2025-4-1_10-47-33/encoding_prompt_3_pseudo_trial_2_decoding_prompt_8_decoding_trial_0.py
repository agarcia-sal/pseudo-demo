def doMain():
    # Step 1: Read two lines of input
    firstInput = input()
    secondInput = input()

    # Step 2: Split the inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Step 3: Initialize a counter for differences
    differenceCount = 0

    # Step 4: Iterate over the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])
        
        # Step 5: Compare the two numbers
        if firstNumber != secondNumber:
            differenceCount += 1

    # Step 6: Check the number of differences and print the result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    doMain()
