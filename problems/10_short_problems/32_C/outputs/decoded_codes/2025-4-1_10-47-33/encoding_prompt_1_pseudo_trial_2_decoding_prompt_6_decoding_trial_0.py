def calculate_remainder_bonus(number, step_size):
    # Calculate how many full groups of step_size fit into number
    full_groups = number // step_size
    
    # Calculate the remainder when number is divided by step_size
    remainder = number % step_size
    
    # Return appropriate value based on the remainder
    if remainder > 0:
        return remainder * (full_groups + 1)
    else:
        return number

# Read a single line of input containing three integers
input_values = input().split()

# Convert input strings to integers
first_number = int(input_values[0])     # First integer
second_number = int(input_values[1])    # Second integer
step_size = int(input_values[2])        # Step size

# Call the function with first_number and step_size
first_result = calculate_remainder_bonus(first_number, step_size)

# Call the function with second_number and step_size
second_result = calculate_remainder_bonus(second_number, step_size)

# Multiply the results and output the final result
final_result = first_result * second_result
print(final_result)
