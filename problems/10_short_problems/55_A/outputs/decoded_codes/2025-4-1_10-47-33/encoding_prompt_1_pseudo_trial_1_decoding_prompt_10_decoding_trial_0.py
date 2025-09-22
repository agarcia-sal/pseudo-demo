def main():
    # Step 1: Get input and initialize variables
    number_of_elements = int(input())
    is_included = [True] * number_of_elements  # Step 2: List of boolean values initialized to True
    current_index = 0
    increment = 1

    # Step 5: Mark elements as False according to the given logic
    while increment <= 500000:
        if is_included[current_index]:  # Only mark if current index is True
            is_included[current_index] = False
        increment += 1
        current_index = (current_index + increment) % number_of_elements  # Update current index

    # Step 6: Filter to find out which indices are still True
    true_values = [value for value in is_included if value]

    # Step 7: Output result based on the length of true_values
    if len(true_values) == 0:
        print("YES")
    else:
        print("NO")

# Run the main function
if __name__ == "__main__":
    main()
