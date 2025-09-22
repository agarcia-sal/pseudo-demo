# Start the program

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
    for index in range(3):  # Assuming we are comparing the first three elements
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        if firstValue != secondValue:
            differenceCount += 1
            
    # Determine the output based on differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# End the program
