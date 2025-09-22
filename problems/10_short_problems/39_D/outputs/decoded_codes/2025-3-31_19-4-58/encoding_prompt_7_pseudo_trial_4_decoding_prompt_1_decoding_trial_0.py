def main():
    # Read two sets of inputs from the user
    firstInput = input()
    secondInput = input()
    
    # Split the inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a counter for differences
    differenceCounter = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):  # Loop from 0 to 2 (inclusive)
        # Convert string elements to integers
        valueFromFirstList = int(firstList[index])
        valueFromSecondList = int(secondList[index])
        
        # Check if the elements are different
        if valueFromFirstList != valueFromSecondList:
            # Increment the difference counter
            differenceCounter += 1 
    
    # Evaluate the number of differences and print the result
    if differenceCounter < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":    
    main()
