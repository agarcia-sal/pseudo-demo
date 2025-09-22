def calculate_modified_product(number1, number2, divisor):
    # Calculate how many full sets of 'divisor' can fit into 'number1' and any remainder
    full_sets1 = number1 // divisor
    remainder1 = number1 % divisor
    
    # If there is a remainder, slightly adjust the value based on its full sets
    if remainder1 > 0:
        adjusted_value1 = remainder1 * (full_sets1 + 1)
    else:
        adjusted_value1 = number1

    # Repeat the same process for 'number2'
    full_sets2 = number2 // divisor
    remainder2 = number2 % divisor
    
    if remainder2 > 0:
        adjusted_value2 = remainder2 * (full_sets2 + 1)
    else:
        adjusted_value2 = number2

    # Return the product of the two adjusted values
    return adjusted_value1 * adjusted_value2

# Main Execution
total1 = int(input())
total2 = int(input())
divisor = int(input())
print(calculate_modified_product(total1, total2, divisor))
