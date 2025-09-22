def mc(number, size):
    """Calculates the adjusted value based on the specified size."""
    quotient, remainder = divmod(number, size)  # Divide number by size
    if remainder > 0:
        return remainder * (quotient + 1)  # Calculate adjusted value if there is a remainder
    else:
        return number  # Return the original number if no remainder

# Read input values for n, m, and s
n = int(input())
m = int(input())
s = int(input())

# Calculate and print the product of adjusted values for n and m
result = mc(n, s) * mc(m, s)
print(result)


  10
  5
  2
  

  20
  

  10
  7
  3
  

  21
  