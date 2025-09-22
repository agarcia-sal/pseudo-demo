# Define Function
def calculate_adjusted_quantity(total_items, divisor):
    # Calculate the quotient and remainder
    quotient = total_items // divisor
    remainder = total_items % divisor
    
    # If remainder is greater than zero
    if remainder > 0:
        return remainder * (quotient + 1)
    # If remainder is zero
    else:
        return total_items

# Main Program Logic
# Read three integers from input
num1 = int(input())
num2 = int(input())
divisor = int(input())

# Call the function for num1 and num2
first_adjusted_value = calculate_adjusted_quantity(num1, divisor)
second_adjusted_value = calculate_adjusted_quantity(num2, divisor)

# Calculate the final result
final_result = first_adjusted_value * second_adjusted_value

# Print the final result
print(final_result)
