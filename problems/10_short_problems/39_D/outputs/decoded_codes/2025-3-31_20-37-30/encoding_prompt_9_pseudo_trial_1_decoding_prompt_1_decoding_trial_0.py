def main():
    # Get input from the user
    print("Enter the first set of values:")
    firstInput = input()
    print("Enter the second set of values:")
    secondInput = input()
    
    # Split the input into lists of values
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Loop through the values in both lists
    for index in range(3):
        # Convert the current values from string to integer
        firstValue = int(firstValues[index])
        secondValue = int(secondValues[index])
        
        # Check if the values are different
        if firstValue != secondValue:
            differenceCount += 1 
    
    # Determine the output based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program
main()
