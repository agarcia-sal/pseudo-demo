# Define Function
def mc(number, divisor):
    q = number // divisor  # Calculate quotient
    r = number % divisor   # Calculate remainder
    if r > 0:              # Check if remainder is greater than 0
        return r * (q + 1)  # Return product of remainder and incremented quotient
    else:
        return number      # Return the original number

# Input Section
total1, total2, divisor = map(int, input().split())

# Processing Section
result1 = mc(total1, divisor)  # Call mc function for total1
result2 = mc(total2, divisor)  # Call mc function for total2

# Output Section
final_product = result1 * result2  # Calculate final product
print(final_product)                # Print the final product
