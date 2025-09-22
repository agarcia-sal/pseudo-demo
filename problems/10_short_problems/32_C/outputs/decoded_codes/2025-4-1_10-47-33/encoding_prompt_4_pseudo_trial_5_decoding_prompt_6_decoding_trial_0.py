# Function to calculate adjusted value based on segments
def mc(number, segment_size):
    # Calculate quotient and remainder
    quotient = number // segment_size
    remainder = number % segment_size
    
    # Return adjusted value based on the remainder
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

# Read input values from standard input
n = int(input())
m = int(input())
s = int(input())

# Calculate results using the mc function
result1 = mc(n, s)
result2 = mc(m, s)

# Print the product of the results
print(result1 * result2)
