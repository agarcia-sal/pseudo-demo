def main():
    # Read two input strings from the user
    firstInput = input()
    secondInput = input()
    
    # Split the inputs into lists of strings
    firstTokens = firstInput.split()
    secondTokens = secondInput.split()
    
    # Initialize a difference counter
    differenceCounter = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the tokens to integers
        firstValue = int(firstTokens[index])
        secondValue = int(secondTokens[index])
        
        # Check if the values are different
        if firstValue != secondValue:
            # Increment the difference counter
            differenceCounter += 1

    # If the number of differences is less than 3
    if differenceCounter < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    main()
