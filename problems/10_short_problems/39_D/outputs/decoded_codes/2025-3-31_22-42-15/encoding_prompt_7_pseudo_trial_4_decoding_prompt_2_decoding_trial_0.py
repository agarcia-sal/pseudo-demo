def checkDifferencesBetweenInputs():
    # Read two strings of space-separated integers from user input
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a variable to count differences
    differenceCount = 0
    
    # Loop over the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the corresponding elements are different
        if firstValue != secondValue:
            # Increment the difference count
            differenceCount += 1
    
    # Decision based on the number of differences counted
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Ensure the function runs only when the script is executed directly
if __name__ == "__main__":
    checkDifferencesBetweenInputs()
