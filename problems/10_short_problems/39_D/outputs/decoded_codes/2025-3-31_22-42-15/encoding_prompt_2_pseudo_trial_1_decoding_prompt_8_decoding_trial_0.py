# Begin the main process
def main():
    # Prompt user for input
    firstInput = input()
    secondInput = input()
    
    # Split inputs into lists
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Initialize difference counter
    differenceCount = 0
    
    # Compare values
    for index in range(3):
        firstValue = int(firstValues[index])
        secondValue = int(secondValues[index])
        
        if firstValue != secondValue:
            differenceCount += 1
            
    # Check if the difference count is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# End the main process and run the program
if __name__ == "__main__":
    main()
