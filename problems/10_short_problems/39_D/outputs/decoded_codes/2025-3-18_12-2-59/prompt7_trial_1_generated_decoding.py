def compareThreeInputs():
    # Read input from the user
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a variable to count the differing elements
    differenceCount = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):  # Loop from 0 to 2
        # Convert the current elements to integers
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])
        
        # Check if the two numbers are different
        if firstNumber != secondNumber:
            # Increment the counter for differences
            differenceCount += 1
    
    # Check if the count of differences is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main execution block
if __name__ == "__main__":
    compareThreeInputs()
