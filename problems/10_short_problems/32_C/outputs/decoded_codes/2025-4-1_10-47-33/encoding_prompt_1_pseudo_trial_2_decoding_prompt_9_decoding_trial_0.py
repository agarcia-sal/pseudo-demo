def calculate_remainder_bonus(number, step_size):
    # Calculate how many full groups of step_size fit into number
    full_groups = number // step_size
    # Calculate the remainder when number is divided by step_size
    remainder = number % step_size
    
    # If there is a remainder, return the product of remainder and (full_groups + 1)
    if remainder > 0:
        return remainder * (full_groups + 1)
    else:
        # Otherwise, return the number itself
        return number

# Read input containing three integers
input_line = input()
first_number, second_number, step_size = map(int, input_line.split())

# Calculate bonuses using the defined function
first_result = calculate_remainder_bonus(first_number, step_size)
second_result = calculate_remainder_bonus(second_number, step_size)

# Calculate the final result by multiplying both bonuses and print it
final_result = first_result * second_result
print(final_result)
