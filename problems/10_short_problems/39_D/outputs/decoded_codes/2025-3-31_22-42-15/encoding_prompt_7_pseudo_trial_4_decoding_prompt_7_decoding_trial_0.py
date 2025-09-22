def checkDifferencesBetweenInputs():
    # Read two strings of space-separated integers from user input
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of strings
    firstList = firstInput.split()  # Convert first input into a list
    secondList = secondInput.split()  # Convert second input into a list
    
    # Initialize a variable to count differences
    differenceCount = 0
    
    # Loop over the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        firstValue = int(firstList[index])  # Convert to integer
        secondValue = int(secondList[index])  # Convert to integer
        
        # Check if the corresponding elements are different
        if firstValue != secondValue:
            # Increment the difference count
            differenceCount += 1
    
    # Decision based on the number of differences counted
    if differenceCount < 3:
        print("YES")  # Output yes if fewer than 3 differences
    else:
        print("NO")  # Output no if 3 or more differences

# Ensure the function runs only when the script is executed directly
if __name__ == "__main__":
    checkDifferencesBetweenInputs()
