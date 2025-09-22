# Step 1: Initialize the total number of test cases
t = int(input())

# Step 2: Set the result variable to count numbers with exactly two distinct prime factors
result = 0

# Step 3: Loop through each number from 1 to t
for i in range(1, t + 1):
    countOfDistinctPrimes = 0  # Step 3.1: Initialize count of distinct prime factors
    currentNumber = i           # Step 3.2: Set currentNumber to i
    
    # Step 3.3: Loop through possible divisors from 2 to i-1
    for j in range(2, i):
        if currentNumber % j == 0:  # Step 3.3.1: Check if currentNumber is divisible by j
            countOfDistinctPrimes += 1  # Step 3.3.1.1: Increment distinct prime count
            
            # Step 3.3.2: While currentNumber is divisible by j
            while currentNumber % j == 0:
                currentNumber //= j  # Step 3.3.2.1: Factor out j completely

    # Step 4: Check if there are exactly two distinct prime factors
    if countOfDistinctPrimes == 2:  # Step 4.1
        result += 1  # Increment result count

# Step 5: Output the final count of numbers with exactly two distinct prime factors
print(result)
