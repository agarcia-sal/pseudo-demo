def doMain():
    # Read inputs from the user
    firstInput = input()
    secondInput = input()
    
    # Split inputs into lists
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize the difference counter
    differenceCount = 0
    
    # Compare values at the first three indices
    for index in range(3):
        valueA = int(firstList[index])
        valueB = int(secondList[index])
        
        # Increment counter if values are different
        if valueA != valueB:
            differenceCount += 1
    
    # Output based on the difference count
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if this script is run directly
if __name__ == "__main__":
    doMain()
