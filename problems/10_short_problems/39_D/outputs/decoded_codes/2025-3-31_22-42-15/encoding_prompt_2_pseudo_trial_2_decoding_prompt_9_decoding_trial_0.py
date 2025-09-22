def main():
    # Prompt the user for input
    firstInput = input()
    secondInput = input()
    
    # Split the input into separate components
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a variable to count differences
    differenceCount = 0
    
    # Compare the components from both input lists
    for index in range(3):
        firstValue = int(firstList[index])  # Convert current item from firstList to integer
        secondValue = int(secondList[index])  # Convert current item from secondList to integer
        
        # Increment the differenceCount if values are not equal
        if firstValue != secondValue:
            differenceCount += 1
    
    # Determine the output based on differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program
main()
