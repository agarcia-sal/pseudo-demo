def main():
    # Read two lines of input from the user
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of strings
    firstTokens = firstInput.split()
    secondTokens = secondInput.split()
    
    # Initialize a counter for differences
    differenceCount = 0 

    # Compare the corresponding elements of the two lists
    for index in range(3):  # Assuming we want to check the first three elements
        # Convert the tokens to integers
        firstValue = int(firstTokens[index])
        secondValue = int(secondTokens[index])
        
        # Check if the values are different
        if firstValue != secondValue:
            differenceCount += 1 
    
    # Determine and print the result based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
