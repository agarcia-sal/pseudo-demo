def mc(number, size):
    # Calculate the quotient and remainder of the division
    q, r = divmod(number, size)
    
    # Adjust the value based on the presence of a remainder
    if r > 0:
        return r * (q + 1)  # If there's a remainder, calculate adjusted value
    else:
        return number  # If there's no remainder, return original number

# Read input values
n = int(input())
m = int(input())
s = int(input())

# Calculate result using the 'mc' function for both n and m
result = mc(n, s) * mc(m, s)

# Output the result
print(result)
