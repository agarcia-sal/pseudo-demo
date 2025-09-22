def main():
    # Prompt the user for input values
    print("Enter first set of numbers:")
    firstInput = input()
    
    print("Enter second set of numbers:")
    secondInput = input()
    
    # Split the input strings into lists of numbers
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    differencesCount = 0  # Initialize a counter for differences

    # Loop through the first three numbers in both lists
    for index in range(3):
        firstNumber = int(firstList[index])    # Convert to integer
        secondNumber = int(secondList[index])   # Convert to integer
        
        # Check if the numbers are different
        if firstNumber != secondNumber:
            differencesCount += 1  # Increment differencesCount by 1
            
    # Check the number of differences found
    if differencesCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
