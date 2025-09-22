def doMain():
    # Read two inputs from the user
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a counter for differing elements
    differenceCount = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the elements are different
        if firstValue != secondValue:
            # Increment the difference counter
            differenceCount += 1 
    
    # Determine output based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    doMain()
