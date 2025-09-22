def mc(n, s):
    # Calculate how many complete groups can be formed
    complete_groups = n // s
    # Calculate the remainder
    remainder = n % s
    
    # Check if there is a remainder
    if remainder > 0:
        return (complete_groups + 1) * remainder
    else:
        return n

# Read input values
n = int(input())
m = int(input())
s = int(input())

# Calculate results for both categories
result_n = mc(n, s)
result_m = mc(m, s)

# Calculate the final output
final_result = result_n * result_m

# Print the final output
print(final_result)
