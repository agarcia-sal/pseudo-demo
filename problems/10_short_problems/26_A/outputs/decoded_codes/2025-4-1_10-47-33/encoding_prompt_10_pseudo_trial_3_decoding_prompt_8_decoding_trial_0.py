# Start Program
t = int(input())  # Input t from the User
res = 0  # Initialize res to 0 (This will hold the count of prime numbers)

# Loop from i = 1 to t (Inclusive)
for i in range(1, t + 1):  
    cnt = 0  # Initialize cnt to 0 (This will count factors of i)
    num = i  # Set num to i (This will be modified to find prime factors)

    # Loop from j = 2 to i - 1
    for j in range(2, i):  
        if num % j == 0:  # If num modulo j equals 0 (j is a factor of num)
            cnt += 1  # Increment cnt by 1 (Count the factor)
            # While num modulo j equals 0
            while num % j == 0:  
                num //= j  # Divide num by j (Remove the factor from num)

    if cnt == 2:  # If cnt equals 2 (i has exactly two distinct prime factors)
        res += 1  # Increment res by 1 (Count this number as prime)

# Output res (Total count of prime numbers)
print(res)  
# End Program


def count_distinct_primes(limit):
    res = 0  # Initialize res to 0 (This will hold the count of prime numbers)

    for i in range(1, limit + 1):
        cnt = 0  # Initialize cnt to 0 (This will count factors of i)
        num = i  # Set num to i (This will be modified to find prime factors)

        for j in range(2, i):
            if num % j == 0:
                cnt += 1
                while num % j == 0:
                    num //= j

        if cnt == 2:
            res += 1

    return res
