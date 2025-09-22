# Read Input
upper_limit = int(input())

# Initialize Counter
pri = 0

# Loop Through Each Number
for cur in range(1, upper_limit + 1):
    # Set divisor count to zero
    div_ct = 0
    tmp = cur

    # Check for Divisors
    for pot in range(2, cur):
        if tmp % pot == 0:  # If tmp is divisible by pot
            div_ct += 1  # Increment divisor count
            # Factor out the divisor
            while tmp % pot == 0:
                tmp //= pot

    # Determine If Prime
    if div_ct == 1:  # If div_ct equals 1, cur is prime
        pri += 1  # Increment prime counter

# Output Result
print(pri)
