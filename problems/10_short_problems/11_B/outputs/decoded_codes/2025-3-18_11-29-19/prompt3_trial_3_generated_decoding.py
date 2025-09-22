def find_index_for_sum():
    # Read the absolute integer input value
    number_to_find = abs(int(input()))  # Read and convert input to an absolute integer

    # Initialize an index variable
    index = 0

    # Start an indefinite loop
    while True:
        # Calculate the sum of the first 'index' natural numbers
        current_sum = (index * (index + 1)) // 2

        # Calculate the difference between the sum and the target number
        difference = current_sum - number_to_find

        # Check if the current sum matches the target number
        if current_sum == number_to_find:
            print(index)  # If it matches, print the index
            break  # Exit the loop

        # Check if the current sum exceeds the target number
        elif current_sum > number_to_find:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # If the difference is even, print the index
                break  # Exit the loop

        # Increment the index for the next iteration
        index += 1

# Run the function to find the index
find_index_for_sum()
