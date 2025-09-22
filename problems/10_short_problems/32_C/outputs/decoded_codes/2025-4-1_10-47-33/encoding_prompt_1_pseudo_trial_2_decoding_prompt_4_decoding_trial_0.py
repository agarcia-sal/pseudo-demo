def calculate_remainder_bonus(number, step_size):
    """Calculate the bonus based on the remainder of a division."""
    full_groups = number // step_size  # Full groups of step_size in number
    remainder = number % step_size      # Remainder when number is divided by step_size
    
    # If there is a remainder, calculate and return the bonus
    if remainder > 0:
        return remainder * (full_groups + 1)
    
    # Return the number itself if no remainder
    return number

# Input handling
input_data = input().strip()  # Read a line of input
first_number, second_number, step_size = map(int, input_data.split())  # Split and convert to integers

# Output calculation
first_result = calculate_remainder_bonus(first_number, step_size)
second_result = calculate_remainder_bonus(second_number, step_size)
final_result = first_result * second_result  # Calculate the final result

# Print the final result
print(final_result)
