def main():
    # Get input from the user
    print("Enter the first set of values:")
    firstInput = input()  # Read first input from user
    print("Enter the second set of values:")
    secondInput = input()  # Read second input from user
    
    # Split the input into lists of values
    firstValues = firstInput.split()  # Split first input string into a list of values
    secondValues = secondInput.split()  # Split second input string into a list of values
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Loop through the values in both lists
    for index in range(3):  # We only compare the first three values
        # Convert the current values from string to integer
        firstValue = int(firstValues[index])  # Convert first value to integer
        secondValue = int(secondValues[index])  # Convert second value to integer
        
        # Check if the values are different
        if firstValue != secondValue:  # If values are not equal
            differenceCount += 1  # Increment the difference counter

    # Determine the output based on the number of differences
    if differenceCount < 3:  # Check if differences are fewer than 3
        print("YES")  # Output YES if the differences are fewer than 3
    else:
        print("NO")  # Output NO otherwise

# Start the program
main()
