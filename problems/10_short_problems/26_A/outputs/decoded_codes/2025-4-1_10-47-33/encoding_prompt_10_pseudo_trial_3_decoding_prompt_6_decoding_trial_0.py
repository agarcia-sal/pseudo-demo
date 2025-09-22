# Start Program

# Declare variable t as an integer and read input from the user
t = int(input())

# Initialize res to 0; this will hold the count of prime numbers
res = 0

# Loop from i = 1 to t (inclusive)
for i in range(1, t + 1):
    # Initialize cnt to 0; this will count distinct prime factors of i
    cnt = 0
    # Set num to i; we'll use num to find prime factors
    num = i
    
    # Loop from j = 2 to i - 1 to check for factors
    for j in range(2, i):
        # If num is divisible by j, j is a distinct prime factor
        if num % j == 0:
            # Increment cnt by 1 for each distinct prime factor found
            cnt += 1
            # While num is divisible by j, keep dividing
            while num % j == 0:
                num //= j  # Remove the factor

    # If cnt equals 1, then i has exactly one distinct prime factor (including itself)
    if cnt == 1:
        # Increment res by 1 to count this number as prime
        res += 1

# Output res (total count of prime numbers)
print(res)

# End Program
