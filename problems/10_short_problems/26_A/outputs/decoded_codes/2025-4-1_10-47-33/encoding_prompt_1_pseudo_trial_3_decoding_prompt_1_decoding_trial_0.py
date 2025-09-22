# Start

# Input: Read an integer value t (representing the upper limit)
t = int(input())

# Initialize result to 0 (to keep track of the count of semi-prime numbers)
result = 0

# For each integer i from 1 to t (inclusive):
for i in range(1, t + 1):
    # Initialize countDivisors to 0 (to count distinct prime factors of i)
    countDivisors = 0
    
    # Set currentNumber to i (to manipulate during factorization)
    currentNumber = i
    
    # For each integer j from 2 to (i-1):
    for j in range(2, i):
        # If currentNumber is divisible by j:
        if currentNumber % j == 0:
            # Increment countDivisors by 1 (found a new prime factor)
            countDivisors += 1
            
            # While currentNumber is divisible by j:
            while currentNumber % j == 0:
                # Divide currentNumber by j (continuing to factor out j)
                currentNumber //= j

    # If countDivisors is equal to 2:
    if countDivisors == 2:
        # Increment result by 1 (i is a semi-prime number)
        result += 1

# Output: Print result (the total count of semi-prime numbers found)
print(result)

# End
