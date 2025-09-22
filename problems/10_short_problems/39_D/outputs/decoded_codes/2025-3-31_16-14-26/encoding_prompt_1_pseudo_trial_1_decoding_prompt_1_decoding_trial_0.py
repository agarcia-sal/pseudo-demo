def main():
    # Read two lines of input from the user
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of values
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Initialize a counter for mismatches
    mismatchCount = 0 
    
    # Loop through the first three values of both lists
    for index in range(3):
        # Convert the string values to integers for comparison
        valueA = int(firstValues[index])
        valueB = int(secondValues[index])
        
        # Check if the values are not equal
        if valueA != valueB:
            # Increment mismatch counter
            mismatchCount += 1 
    
    # Check the number of mismatches
    if mismatchCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program runs
main()
