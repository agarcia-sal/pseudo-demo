def calculate_remainder_bonus(number, step_size):
    # Calculate the number of full groups that fit into 'number'
    full_groups = number // step_size
    # Calculate the remainder of 'number' divided by 'step_size'
    remainder = number % step_size

    # Check if there is a remainder and calculate the bonus accordingly
    if remainder > 0:
        return remainder * (full_groups + 1)
    else:
        return number

# Read input as a single line and split it into three integers
input_line = input()
first_number, second_number, step_size = map(int, input_line.split())

# Calculate results using the defined function
first_result = calculate_remainder_bonus(first_number, step_size)
second_result = calculate_remainder_bonus(second_number, step_size)

# Calculate the final result by multiplying the two results and print it
final_result = first_result * second_result
print(final_result)
