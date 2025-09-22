def find_smallest_non_negative_integer(target_number):
    # Get the absolute value of the target number
    target_number = abs(target_number)
    index = 0

    while True:
        # Calculate the sum of integers from 0 to index using the formula
        sum_to_index = (index * (index + 1)) // 2
        
        # Calculate the difference
        difference = sum_to_index - target_number
        
        # Check for an exact match
        if sum_to_index == target_number:
            print(index)
            break
        
        # Check if the sum exceeds the target number
        if sum_to_index > target_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment index for the next iteration
        index += 1

# Example usage:
# Call the function without parameters and provide input in the next line after running
target = int(input())
find_smallest_non_negative_integer(target)
