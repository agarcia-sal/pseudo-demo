def main():
    # Read an integer input representing the size of the array
    sizeOfArray = int(input())
    
    # Initialize a boolean array where all elements are set to true
    booleanArray = [True] * sizeOfArray
    
    # Set initial values for index variables
    indexForIncrement = 0
    counter = 1
    
    # Iterate a maximum of 500,000 times
    while counter <= 500000:
        # If the current position in the boolean array is true
        if booleanArray[indexForIncrement]:
            # Mark the current position as false
            booleanArray[indexForIncrement] = False
        
        # Update the counter for the next iteration
        counter += 1
        
        # Calculate the next index using modulo operation
        indexForIncrement = (indexForIncrement + counter) % sizeOfArray

    # Create a new list containing only true values from the boolean array
    trueValuesList = [value for value in booleanArray if value]
    
    # Check if the list of true values is empty
    if len(trueValuesList) == 0:
        # Print 'YES' if there are no true values remaining
        print('YES')
    else:
        # Print 'NO' if there are still true values
        print('NO')

# Call the main function
main()
