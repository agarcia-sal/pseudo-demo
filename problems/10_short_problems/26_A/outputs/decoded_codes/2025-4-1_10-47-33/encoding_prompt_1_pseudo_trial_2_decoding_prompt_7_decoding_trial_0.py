# Initialize the total number of test cases by reading an integer input
t = int(input())

# Set the variable `result` to 0, which will store the count of numbers that have exactly two distinct prime factors
result = 0

# Loop through each number `i` from 1 to `t` (inclusive)
for i in range(1, t + 1):
    # Initialize a count variable `countOfDistinctPrimes` to 0
    countOfDistinctPrimes = 0
    # Set a variable `currentNumber` equal to `i`, which will be factored
    currentNumber = i

    # For each possible divisor `j` starting from 2 up to `i - 1`
    for j in range(2, i):
        # If `currentNumber` is divisible by `j`
        if currentNumber % j == 0:
            # Increment `countOfDistinctPrimes` by 1
            countOfDistinctPrimes += 1
            # While `currentNumber` is still divisible by `j`
            while currentNumber % j == 0:
                # Divide `currentNumber` by `j` to completely factor out this prime factor
                currentNumber //= j
        
        # If we already found two distinct prime factors, break out of the loop
        if countOfDistinctPrimes > 2:
            break
    
    # If `countOfDistinctPrimes` equals 2
    if countOfDistinctPrimes == 2:
        # Increment `result` by 1
        result += 1

# Output the final count of numbers with exactly two distinct prime factors
print(result)
