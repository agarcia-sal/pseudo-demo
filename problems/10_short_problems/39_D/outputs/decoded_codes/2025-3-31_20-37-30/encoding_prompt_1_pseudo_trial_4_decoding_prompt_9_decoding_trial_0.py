def main():
    # Receive input from the user
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize difference counter
    differenceCount = 0

    # Compare corresponding elements in both lists
    for index in range(3):  # Loop through the first three indices
        # Convert elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the values are different
        if firstValue != secondValue:
            differenceCount += 1
    
    # Determine output based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute main function if script is run as the main program
if __name__ == "__main__":
    main()
