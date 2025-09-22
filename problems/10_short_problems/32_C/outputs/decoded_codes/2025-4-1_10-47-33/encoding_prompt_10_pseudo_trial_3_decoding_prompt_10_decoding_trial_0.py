def mc(n, s):
    """Calculate an extended value based on input n and divisor s."""
    quotient, remainder = divmod(n, s)  # Use divmod for quotient and remainder
    
    if remainder > 0:
        return remainder * (quotient + 1)  # Calculate extended value when there is a remainder
    else:
        return n  # Return n if there is no remainder

# Read input values for n, m, and s
n = int(input())
m = int(input())
s = int(input())

# Calculate the product of mc(n, s) and mc(m, s)
result = mc(n, s) * mc(m, s)

# Output the result
print(result)


   10
   20
   5
   

   7
   8
   3
   

   0
   12
   1
   