def find_smallest_integer(target_number):
    """Finds the smallest non-negative integer whose sum of numbers up to that integer
    either equals the target number or exceeds it with an even difference."""
    
    # Initialize the index to start checking from 0
    index = 0

    # Continue indefinitely until we find a valid index 
    while True:
        # Calculate the sum of integers from 0 to index using the formula
        sum_to_index = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the target number
        difference = sum_to_index - target_number

        # Check if the calculated sum equals the target number
        if sum_to_index == target_number:
            print(index)
            break
        
        # Check if the sum exceeds the target number and the difference is even
        if sum_to_index > target_number:
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment the index for the next iteration
        index += 1

# Example usage:
target_number = abs(int(input()))
find_smallest_integer(target_number)
