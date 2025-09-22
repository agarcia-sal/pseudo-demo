def main():
    # Receive input for the first set of values
    firstValueSet = input()
    # Receive input for the second set of values
    secondValueSet = input()
    
    # Split the input strings into lists of values
    firstValues = firstValueSet.split()
    secondValues = secondValueSet.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Compare each corresponding value in the two sets
    for index in range(3):  # Loop for three values
        firstNumber = int(firstValues[index])  # Convert to integer
        secondNumber = int(secondValues[index])  # Convert to integer
        
        # Check if the numbers are different
        if firstNumber != secondNumber:
            differenceCount += 1  # Increment counter for differences
            
    # Output decision based on the count of differences
    if differenceCount < 3:
        print("YES")  # Fewer than three differences
    else:
        print("NO")   # Three or more differences

# Call the main function if this script is executed
if __name__ == "__main__":
    main()
