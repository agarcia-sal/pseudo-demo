def main():
    # Input: read an integer n from user input
    n = int(input())
    
    # Initialize a boolean array of size n with all values set to True
    is_processed = [True] * n

    # Initialize counters
    current_index = 0  # represents the current index in the array
    iteration_count = 1  # represents the current iteration number

    # Loop until the limit of 500,000
    while iteration_count <= 500000:
        # Check boolean condition
        if is_processed[current_index]:
            # Mark index current_index as processed
            is_processed[current_index] = False
        
        # Increment the iteration count
        iteration_count += 1
        # Update the current_index to the next index in a circular manner
        current_index = (current_index + iteration_count) % n

    # Filter True values: create a list of indices which are still True
    remaining_true_values = [value for value in is_processed if value]

    # Output result
    if len(remaining_true_values) == 0:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    main()
