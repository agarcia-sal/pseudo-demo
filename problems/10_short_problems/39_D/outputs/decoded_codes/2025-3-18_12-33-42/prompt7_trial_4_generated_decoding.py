def doMain():
    # Read input values from the user
    firstInput = input().strip()
    secondInput = input().strip()
    
    # Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Iterate over the components of the inputs (assumes both lists have 3 components)
    for index in range(3):
        # Convert the string elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check for differences between the values
        if firstValue != secondValue:
            differenceCount += 1
    
    # Determine if less than 3 differences were found
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main program execution
if __name__ == "__main__":
    doMain()
