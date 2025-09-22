# Step 1: Input - Read the upper limit for checking prime numbers
t = int(input())

# Step 2: Initialize Result
primeCount = 0  # Variable to count prime numbers

# Step 3: Loop Through Numbers
for i in range(1, t + 1):  # Loop from 1 to t (inclusive)
    divisorCount = 0  # Initialize the count of divisors
    currentNumber = i  # Set currentNumber to i

    # Step 4: Check for Divisors
    for j in range(2, i):  # Loop from 2 to (i - 1)
        if currentNumber % j == 0:  # If currentNumber is divisible by j
            divisorCount += 1  # Increment divisor count
            while currentNumber % j == 0:  # While divisible by j
                currentNumber //= j  # Reduce currentNumber

    # Step 5: Determine Primality
    if divisorCount == 2:  # If it has exactly 2 distinct divisors
        primeCount += 1  # Increment prime count

# Step 6: Output - Print the total number of prime numbers found
print(primeCount)
