def mc(number, size):
    # Calculate quotient and remainder when dividing number by size
    quotient = number // size
    remainder = number % size
    
    # If remainder exists, calculate the adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)  # Adjusted value
    else:
        return number  # Return the original number if no remainder

# Read input values
n = int(input())
m = int(input())
s = int(input())

# Calculate result using the 'mc' function for both n and m
result = mc(n, s) * mc(m, s)

# Output the result
print(result)
