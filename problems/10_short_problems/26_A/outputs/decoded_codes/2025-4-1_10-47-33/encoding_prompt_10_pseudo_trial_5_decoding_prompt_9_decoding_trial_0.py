# Read the integer for the number of test cases
t = int(input())

# Initialize a variable to store the count of prime numbers
res = 0

# Loop through each number from 1 to t
for i in range(1, t + 1):
    cnt = 0  # Initialize a counter for factors
    num = i  # Set variable num to i

    # Check for factors of num
    for j in range(2, i):
        if num % j == 0:  # Check if num is divisible by j
            cnt += 1  # Increment factor count
            # While num is divisible by j, divide num by j
            while num % j == 0:
                num //= j
    
    # Determine if i is a prime number
    if cnt == 1:  # If cnt equals 1, it means the number is prime
        res += 1  # Increment the prime count

# Output the total count of prime numbers found
print(res)
