def main():
    # Step 1: Read an integer n from input
    n = int(input())

    # Step 2: Initialize a list to track boolean values
    boolean_list = [True] * n

    # Step 3: Initialize indices
    current_index = 0
    counter = 1

    # Step 4: Loop until counter exceeds 500000
    while counter <= 500000:
        # Step 5: If the current index in the boolean list is True
        if boolean_list[current_index]:
            # Step 6: Set the current index to False
            boolean_list[current_index] = False

        # Step 7: Increment counter
        counter += 1
        
        # Step 8: Update current index using modular arithmetic
        current_index = (current_index + counter) % n

    # Step 9: Filter out the True values from the boolean list
    filtered_list = [value for value in boolean_list if value]

    # Step 10: Check the length of the filtered list
    if len(filtered_list) == 0:
        print("YES")  # All positions were marked False
    else:
        print("NO")   # There are still True positions left

# Call the main function to execute the code
if __name__ == "__main__":
    main()
