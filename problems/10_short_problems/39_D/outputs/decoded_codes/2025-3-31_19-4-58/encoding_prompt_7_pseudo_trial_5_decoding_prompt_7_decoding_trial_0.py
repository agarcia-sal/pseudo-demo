def compareThreeInputs():
    # Prompt user for first input
    firstInput = input()
    
    # Prompt user for second input
    secondInput = input()
    
    # Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a difference counter
    differenceCount = 0 

    # Iterate over the first three elements of both lists
    for index in range(3):
        # Convert the current elements from string to integer
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])

        # Check if there's a difference between the two numbers
        if firstNumber != secondNumber:
            # Increment the difference count by 1 
            differenceCount += 1 
    
    # Determine if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if program is run directly
if __name__ == "__main__":
    compareThreeInputs()
