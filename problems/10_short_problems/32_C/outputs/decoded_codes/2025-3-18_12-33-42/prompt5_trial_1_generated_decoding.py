def mc(number, divisor):
    # Calculate the number of complete groups
    complete_groups = number // divisor  # Quotient of the division
    remainder = number % divisor           # Remainder of the division

    # Determine the effective size of the last group
    if remainder > 0:
        return remainder * (complete_groups + 1)  # Non-full group contributes
    else:
        return number  # Fits exactly into the groups

# Main function execution
# Read input values: n, m, and s
n = int(input())
m = int(input())
s = int(input())

# Calculate values using mc function
result1 = mc(n, s)
result2 = mc(m, s)

# Calculate final output
final_result = result1 * result2

# Display the final result
print(final_result)
