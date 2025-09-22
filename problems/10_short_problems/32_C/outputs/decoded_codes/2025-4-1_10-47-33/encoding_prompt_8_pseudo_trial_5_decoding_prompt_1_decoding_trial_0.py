def calculate_modified_value(total, divisor):
    quotient = total // divisor  # Get the whole number result of division
    remainder = total % divisor   # Get the remainder of the division
    if remainder > 0:
        return remainder * (quotient + 1)  # Calculate modified value if remainder exists
    else:
        return total  # Return the original total if no remainder

# Main program
n = int(input())  # Read n from input
m = int(input())  # Read m from input
s = int(input())  # Read s from input
modified_n = calculate_modified_value(n, s)  # Call function for n
modified_m = calculate_modified_value(m, s)  # Call function for m
final_result = modified_n * modified_m  # Calculate final result
print(final_result)  # Print the final result
