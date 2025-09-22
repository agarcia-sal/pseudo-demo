def main():
    # Read input values from the user
    firstInput = input()  # First set of numbers
    secondInput = input()  # Second set of numbers
    
    # Split the input strings into lists of numbers
    firstList = firstInput.split()  # Split to create a list of string numbers
    secondList = secondInput.split()  # Split to create a list of string numbers
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Compare elements from both lists
    for index in range(3):  # Loop over the first 3 indices
        # Convert string elements to integers
        firstNumber = int(firstList[index])  # Convert to integer
        secondNumber = int(secondList[index])  # Convert to integer
        
        # If numbers differ, increment the difference counter
        if firstNumber != secondNumber:
            differenceCount += 1  # Increment the count of differences
    
    # Check the number of differences and print the result
    if differenceCount < 3:
        print("YES")  # Fewer than 3 elements differ
    else:
        print("NO")  # 3 or more elements differ

# Execute the main function if this file is run directly
if __name__ == "__main__":
    main()
