def find_smallest_integer(target_number):
    # Initialize variables
    target_number = abs(target_number)  # Taking the absolute value of the input number
    index = 0  # Starting index

    while True:  # Start an infinite loop
        # Calculate the sum of all integers from 0 to index
        sum_to_index = (index * (index + 1)) // 2

        # Calculate the difference between sum_to_index and target_number
        difference = sum_to_index - target_number

        # Check if we found an exact match
        if sum_to_index == target_number:
            print(index)  # Print the current index
            break  # Exit the loop

        # Check if the sum exceeds the target number
        if sum_to_index > target_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Print the current index
                break  # Exit the loop

        # Increment the index
        index += 1

# Example usage:
target_number = int(input())  # Read input without prompt
find_smallest_integer(target_number)
