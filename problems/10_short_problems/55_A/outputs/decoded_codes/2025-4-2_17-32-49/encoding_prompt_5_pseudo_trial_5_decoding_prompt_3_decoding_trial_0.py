def main():
    # Step 2: Input Section
    n = int(input())  # Read an integer input for the number of elements

    # Step 3: Initialization
    boolean_list = [True] * n  # Create a list of n True values
    current_index = 0
    counter = 1

    # Step 4: Loop for Operations
    while counter <= 500000:
        if boolean_list[current_index]:  # Check if the current element is True
            boolean_list[current_index] = False  # Set it to False
        
        counter += 1  # Increment the counter
        # Update the current index using modulo to wrap around
        current_index = (current_index + counter) % n

    # Step 5: Check Remaining True Values
    remaining_true = [value for value in boolean_list if value]  # Get all True elements

    # Determine output based on the presence of remaining True values
    if len(remaining_true) == 0:
        print("YES")  # All values have been set to False
    else:
        print("NO")   # Some values are still True

# Execute the main function
if __name__ == "__main__":
    main()
