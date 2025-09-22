def calculate_remainder_bonus(number, step_size):
    """Calculate the remainder bonus based on the number and step size."""
    full_groups = number // step_size
    remainder = number % step_size
    
    if remainder > 0:
        return remainder * (full_groups + 1)
    
    return number

def main():
    # Read a single line of input containing three integers
    input_values = input().split()
    first_number = int(input_values[0])
    second_number = int(input_values[1])
    step_size = int(input_values[2])
    
    # Calculate results using the defined function
    first_result = calculate_remainder_bonus(first_number, step_size)
    second_result = calculate_remainder_bonus(second_number, step_size)
    
    # Output the final multiplied result
    final_result = first_result * second_result
    print(final_result)

if __name__ == "__main__":
    main()
