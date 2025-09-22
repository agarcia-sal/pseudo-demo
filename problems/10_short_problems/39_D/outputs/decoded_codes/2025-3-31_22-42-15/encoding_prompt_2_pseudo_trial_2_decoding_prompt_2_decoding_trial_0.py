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
    for i in range(3):  # Assuming the lists have at least 3 items
        firstValue = int(firstList[i])
        secondValue = int(secondList[i])
        if firstValue != secondValue:
            differenceCount += 1
    
    # Determine the output based on differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program
main()
