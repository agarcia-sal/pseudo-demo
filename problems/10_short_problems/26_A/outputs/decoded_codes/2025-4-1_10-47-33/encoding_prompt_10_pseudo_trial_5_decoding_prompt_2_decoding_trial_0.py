# Step 1: Read integer t from user input
t = int(input())

# Step 2: Initialize count of prime numbers
res = 0

# Step 3: Loop through each number from 1 to t
for i in range(1, t + 1):
    cnt = 0  # Initialize counter for factors
    num = i  # Set num to the current number i

    # Step 4: Check for factors of num
    for j in range(2, i):  # Loop from 2 to i-1
        if num % j == 0:  # If num is divisible by j
            cnt += 1  # Increment factor count
            # While num is divisible by j
            while num % j == 0:
                num //= j  # Divide num by j

    # Step 5: Determine if i is a prime number
    if cnt == 1:  # Corrected the condition to check for exactly 1 distinct factor (which is j)
        res += 1  # Increment the prime count

# Step 6: Output the total count of prime numbers found
print(res)
