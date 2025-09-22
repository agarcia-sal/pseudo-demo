# Step 1: Read Input
upper_limit = int(input())  # Get an integer value from the user to represent the upper limit of the range.

# Step 2: Initialize Counter
pri = 0  # Variable to count prime numbers.

# Step 3: Loop Through Each Number
for cur in range(1, upper_limit + 1):  # Loop from 1 to the upper limit (inclusive).
    div_ct = 0  # Initialize the divisor count to zero for the current number.
    tmp = cur  # Temporary variable set to the current number.

    # Step 4: Check for Divisors
    for pot in range(2, cur):  # Loop through possible divisors from 2 to cur-1.
        if tmp % pot == 0:  # Check if tmp is divisible by pot.
            div_ct += 1  # Increment the divisor count.
            while tmp % pot == 0:  # Factor out the divisor.
                tmp //= pot  # Divide tmp by pot.

    # Step 5: Determine If Prime
    if div_ct == 1:  # If there is exactly one divisor found
        pri += 1  # Increment the prime count.

# Step 6: Output Result
print(pri)  # Print the total number of prime numbers found.
