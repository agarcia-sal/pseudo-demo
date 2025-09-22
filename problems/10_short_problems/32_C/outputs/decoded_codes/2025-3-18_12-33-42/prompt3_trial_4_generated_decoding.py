def mc(number, size):
    # Calculate quotient and remainder when dividing number by size
    quotient, remainder = divmod(number, size)
    
    if remainder > 0:
        # If there is a remainder, return the total considering the extra portion
        return remainder * (quotient + 1)
    else:
        # If no remainder, return the original number
        return number

# Read input values for n, m, and s
n = int(input())
m = int(input())
s = int(input())

# Calculate the product of the results from mc function for n and m, and print the result
result = mc(n, s) * mc(m, s)
print(result)
