# Step 1: Read the number of test cases.
t = int(input())

# Step 2: Initialize a variable to store the count of prime numbers.
res = 0

# Step 3: Loop through each number from 1 to t.
for i in range(1, t + 1):
    # Initialize a counter for the number of factors.
    cnt = 0
    num = i

    # Step 4: Check for factors of num.
    for j in range(2, i):
        if num % j == 0:
            cnt += 1
            # While num is divisible by j.
            while num % j == 0:
                num //= j

    # Step 5: Determine if i is a prime number.
    if cnt == 1:  # A prime number has exactly one distinct factor (itself).
        res += 1

# Step 6: Output the total count of prime numbers found.
print(res)


def is_prime(num):
    if num < 2:
        return False
    for j in range(2, int(num**0.5) + 1):
        if num % j == 0:
            return False
    return True

t = int(input())
res = 0
for i in range(1, t + 1):
    if is_prime(i):
        res += 1

print(res)
