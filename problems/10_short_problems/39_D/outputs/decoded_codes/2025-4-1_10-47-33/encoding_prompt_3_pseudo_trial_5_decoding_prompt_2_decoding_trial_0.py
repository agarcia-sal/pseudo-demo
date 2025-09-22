def doMain():
    # Read two lines of input from the user
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of components
    componentsFromFirstInput = firstInput.split()
    componentsFromSecondInput = secondInput.split()
    
    # Initialize a variable to count the number of differences
    differenceCount = 0 
    
    # Loop through the first three items of both lists
    for index in range(3):
        # Convert the components at the current index from string to integer
        valueFromFirstInput = int(componentsFromFirstInput[index])
        valueFromSecondInput = int(componentsFromSecondInput[index])
        
        # Check if the values are different
        if valueFromFirstInput != valueFromSecondInput:
            # Increment the difference counter
            differenceCount += 1 
    
    # After checking all components, determine if the result is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start of the program execution
if __name__ == "__main__":
    doMain()
