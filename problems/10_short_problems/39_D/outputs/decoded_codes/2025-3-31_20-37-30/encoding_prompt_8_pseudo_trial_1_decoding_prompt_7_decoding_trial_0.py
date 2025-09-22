def main():
    # Prompt the user for input values
    print("Enter first set of numbers:")
    firstInput = input()  # First set of numbers input from the user
    print("Enter second set of numbers:")
    secondInput = input()  # Second set of numbers input from the user
    
    # Split the input strings into lists of strings using space as delimiter
    firstList = firstInput.split()  # Create a list of the first set
    secondList = secondInput.split()  # Create a list of the second set
    
    differencesCount = 0  # Initialize a counter for differences

    # Loop through the first three numbers in both lists
    for index in range(3):  # Only compare the first three indices
        firstNumber = int(firstList[index])  # Convert first number to integer
        secondNumber = int(secondList[index])  # Convert second number to integer
        
        # Check if the numbers are different
        if firstNumber != secondNumber:  # Compare the two numbers
            differencesCount += 1  # Increment the count of differences
            
    # Check the number of differences found
    if differencesCount < 3:  # If differences are less than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Otherwise output "NO"

# Execute the main function
main()
