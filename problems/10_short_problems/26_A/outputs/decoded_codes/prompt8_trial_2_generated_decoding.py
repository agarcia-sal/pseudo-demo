def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Take an integer input from the user representing the upper limit
t = int(input())

# Initialize a variable to count the number of prime numbers
primeCount = 0

# Loop through each number from 1 to t (inclusive)
for i in range(1, t + 1):
    # Check if the current number is prime
    if is_prime(i):
        # Increment the total prime count
        primeCount += 1

# Output the total count of prime numbers found
print(primeCount)
