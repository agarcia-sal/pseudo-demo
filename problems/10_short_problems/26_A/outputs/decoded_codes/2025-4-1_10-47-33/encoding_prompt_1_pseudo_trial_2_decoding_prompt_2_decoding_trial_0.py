# Step 1: Initialize the total number of test cases by reading an integer input t.
t = int(input())

# Step 2: Set the variable result to 0.
result = 0

# Step 3: For each number i from 1 to t (inclusive)
for i in range(1, t + 1):
    # Step 3.1: Initialize countOfDistinctPrimes to 0.
    countOfDistinctPrimes = 0
    # Step 3.2: Set currentNumber equal to i.
    currentNumber = i

    # Step 3.3: For each possible divisor j starting from 2 up to i - 1
    for j in range(2, i):
        # Step 3.3.1: If currentNumber is divisible by j
        if currentNumber % j == 0:
            # Step 3.3.1.1: Increment countOfDistinctPrimes by 1.
            countOfDistinctPrimes += 1
            # Step 3.3.1.2: While currentNumber is still divisible by j
            while currentNumber % j == 0:
                # Step 3.3.1.2.1: Divide currentNumber by j.
                currentNumber //= j

    # Step 3.4: If countOfDistinctPrimes equals 2
    if countOfDistinctPrimes == 2:
        # Step 3.4.1: Increment result by 1.
        result += 1

# Step 4: Output the final count of numbers with exactly two distinct prime factors.
print(result)
