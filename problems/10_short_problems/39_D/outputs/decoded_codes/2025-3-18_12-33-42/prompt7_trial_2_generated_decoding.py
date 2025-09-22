def main():
    # Read input from user
    firstInput = input()
    secondInput = input()
    
    # Split input strings into lists of numbers (as strings)
    firstNumbers = firstInput.split()
    secondNumbers = secondInput.split()
    
    # Initialize a counter for the differences
    differenceCount = 0 

    # Loop over the range of indices (0 to 2) to compare numbers
    for index in range(3):  # Iterating through the first three elements
        # Convert the strings to integers for comparison
        numberA = int(firstNumbers[index])
        numberB = int(secondNumbers[index])
        
        # Increment the difference counter if numbers are not equal
        if numberA != numberB:
            differenceCount += 1
            
    # Check the number of differences and print the appropriate response
    if differenceCount < 3:
        print("YES")  # Fewer than three differences
    else:
        print("NO")   # Three or more differences

# Check if this script is the main module and call main function
if __name__ == "__main__":
    main()
