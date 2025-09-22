def main():
    # Read an integer input for the size of the array
    n = int(input())

    # Initialize an array of boolean values all set to True
    boolean_array = [True] * n

    # Initialize two counters
    j = 0
    i = 1

    # Loop until i exceeds 500000
    while i <= 500000:
        # If the current position j in array boolean_array is True
        if boolean_array[j]:
            # Set the value at position j in array boolean_array to False
            boolean_array[j] = False
        
        # Increment i
        i += 1
        
        # Update j to the new position
        j = (j + i) % n

    # Create a new list x with all values in boolean_array that are still True
    true_values = [value for value in boolean_array if value]

    # Check if list true_values is empty
    if len(true_values) == 0:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()
