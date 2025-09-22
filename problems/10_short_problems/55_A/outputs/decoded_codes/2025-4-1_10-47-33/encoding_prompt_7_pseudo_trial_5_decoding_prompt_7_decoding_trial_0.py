def checkIfAllFalse(n):
    # INPUT: An integer n indicating the size of a boolean list
    # OUTPUT: Prints 'YES' if all values in the list are False, otherwise prints 'NO'

    # Initialize a list of boolean values all set to True
    booleanList = [True] * n
    index = 0  # Start from the first index
    step = 1  # Initial step value

    # Iterate while step is less than or equal to 500000
    while step <= 500000:
        # If the current position in the booleanList is True
        if booleanList[index]:
            # Set the current position to False
            booleanList[index] = False
        
        # Increment step for the next iteration
        step += 1

        # Update index using circular indexing based on step
        index = (index + step) % n

    # Filter the booleanList to find all remaining True values
    remainingTrue = [val for val in booleanList if val]

    # If there are no True values remaining
    if len(remainingTrue) == 0:
        print('YES')
    else:
        print('NO')

# Example usage and testing
if __name__ == "__main__":
    # Test with different cases
    checkIfAllFalse(5)  # Test with a small n
    checkIfAllFalse(10) # Test with a larger n
    checkIfAllFalse(100) # Test for scalability and performance
