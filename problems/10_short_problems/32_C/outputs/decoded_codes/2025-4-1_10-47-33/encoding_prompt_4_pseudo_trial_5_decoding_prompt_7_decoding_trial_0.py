def mc(number, segmentSize):
    # Calculate the quotient and remainder by dividing number by segmentSize
    quotient = number // segmentSize
    remainder = number % segmentSize
    
    # If there is a remainder, return the adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number  # Return the original number if no remainder

# Read input values for n, m, and s from standard input
n = int(input())  # Read first value and convert to integer
m = int(input())  # Read second value and convert to integer
s = int(input())  # Read third value and convert to integer

# Calculate the result for both n and m using the mc function
result1 = mc(n, s)
result2 = mc(m, s)

# Print the product of the two results
print(result1 * result2)
