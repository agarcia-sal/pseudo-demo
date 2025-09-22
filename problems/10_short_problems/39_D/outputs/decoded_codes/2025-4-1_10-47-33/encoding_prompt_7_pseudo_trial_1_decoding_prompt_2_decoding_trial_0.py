def main():
    # Read input values for two sets of data
    firstInput = input()
    secondInput = input()
    
    # Split the input values into lists
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a variable to count differences
    differenceCount = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert elements to integers
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])
        
        # Check if the numbers are different
        if firstNumber != secondNumber:
            # Increment the difference count
            differenceCount += 1
            
    # Determine if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")


# Entry point of the program
if __name__ == "__main__":
    main()
