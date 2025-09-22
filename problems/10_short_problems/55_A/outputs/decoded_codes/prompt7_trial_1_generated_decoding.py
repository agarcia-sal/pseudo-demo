def checkCondition(n):
    # Initialize an array to track boolean values
    booleanArray = [True] * n
    j = 0  # Initialize index j for the boolean array
    i = 1  # Initialize counter i

    # Iterate through a range up to 500,000
    while i <= 500000:
        # If the current position in the boolean array is True
        if booleanArray[j]:
            # Mark this position as False
            booleanArray[j] = False

        # Increment counter i
        i += 1
        
        # Update index j using modulo operation to wrap around
        j = (j + i) % n

    # Collect all True values from the boolean array
    trueValues = [value for value in booleanArray if value]

    # Check if there are any remaining True values
    if len(trueValues) == 0:
        print('YES')
    else:
        print('NO')

# Example of using the function with input
n = int(input())
checkCondition(n)
