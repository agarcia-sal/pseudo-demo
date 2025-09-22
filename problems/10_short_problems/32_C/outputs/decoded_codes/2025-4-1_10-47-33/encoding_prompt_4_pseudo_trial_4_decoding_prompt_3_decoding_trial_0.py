def mc(number, size):
    # Calculate quotient and remainder when dividing 'number' by 'size'
    quotient, remainder = divmod(number, size)
    
    # If remainder exists, calculate and return adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number  # Return the original number when no remainder

# Read input values
n = int(input())
m = int(input())
s = int(input())

# Calculate result using the 'mc' function for both n and m
result = mc(n, s) * mc(m, s)

# Output the result
print(result)
