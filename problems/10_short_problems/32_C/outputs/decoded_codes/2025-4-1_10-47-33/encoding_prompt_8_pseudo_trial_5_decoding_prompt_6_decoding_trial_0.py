def calculate_modified_value(total, divisor):
    # Divide total by divisor to get quotient and remainder
    quotient = total // divisor
    remainder = total % divisor
    
    # Return adjusted value based on the existence of a remainder
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total

# Main program starts here
n = int(input())  # Read integer value for n
m = int(input())  # Read integer value for m
s = int(input())  # Read integer value for s

# Calculate modified values for n and m based on s
modified_n = calculate_modified_value(n, s)
modified_m = calculate_modified_value(m, s)

# Calculate the final result as product of modified_n and modified_m
final_result = modified_n * modified_m

# Print the final result
print(final_result)
