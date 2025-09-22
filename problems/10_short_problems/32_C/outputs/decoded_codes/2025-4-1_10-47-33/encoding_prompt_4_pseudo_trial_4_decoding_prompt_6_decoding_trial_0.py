# Define the mc function which processes the number based on size
def mc(number, size):
    # Calculate quotient and remainder
    quotient = number // size
    remainder = number % size
    
    # Adjust value based on remainder
    if remainder > 0:
        return remainder * (quotient + 1)  # If remainder exists, calculate adjusted value
    else:
        return number  # Return original number if no remainder

# Read input values
n = int(input())  # Read an integer for n
m = int(input())  # Read an integer for m
s = int(input())  # Read an integer for s

# Calculate result using the mc function for both n and m
result = mc(n, s) * mc(m, s)

# Output the result
print(result)
