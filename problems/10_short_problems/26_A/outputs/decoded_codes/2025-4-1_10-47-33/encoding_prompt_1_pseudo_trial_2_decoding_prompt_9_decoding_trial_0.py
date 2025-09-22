# Initialize the total number of test cases by reading an integer input t
t = int(input())

# Set the variable result to 0, which will store the count of numbers
# that have exactly two distinct prime factors
result = 0

# Iterate over each number i from 1 to t (inclusive)
for i in range(1, t + 1):
    # Initialize a count variable to track the number of distinct prime factors of i
    countOfDistinctPrimes = 0
    currentNumber = i  # Set the number to be factored

    # Check for each possible divisor from 2 up to i - 1
    for j in range(2, i):
        # If currentNumber is divisible by j
        if currentNumber % j == 0:
            # Increment the count of distinct primes
            countOfDistinctPrimes += 1
            
            # While currentNumber is divisible by j, divide it to factor out j
            while currentNumber % j == 0:
                currentNumber //= j  # integer division
            
    # If there are exactly two distinct prime factors, increment the result
    if countOfDistinctPrimes == 2:
        result += 1

# Output the final count of numbers with exactly two distinct prime factors
print(result)
