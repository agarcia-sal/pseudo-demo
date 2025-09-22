# Step 1: Receive integer input for the upper limit
t = int(input())

# Step 2: Initialize the counter for semi-primes
result = 0

# Step 3: Loop through each number from 1 to t
for i in range(1, t + 1):
    count = 0  # Counter for distinct prime factors
    current_number = i  # Number to analyze

    # Step 4: Check for factors starting from 2
    for j in range(2, i):
        if current_number % j == 0:  # Check if j is a factor
            count += 1  # Found a new distinct prime factor
            # Eliminate all occurrences of the prime factor j
            while current_number % j == 0:
                current_number //= j  # Integer division

    # Step 5: Check if the count of distinct prime factors is exactly 2
    if count == 2:
        result += 1  # Increment the semi-prime count

# Step 6: Output the total count of semi-primes
print(result)
