# Read an integer input that represents the upper limit for checking prime numbers
t = int(input())

# Initialize a variable to keep track of the count of prime numbers found
prime_count = 0

# Function to find the number of unique prime factors of a number
def unique_prime_factors_count(n):
    count = 0
    current_number = n
    for j in range(2, n):
        if current_number % j == 0:
            count += 1
            while current_number % j == 0:
                current_number //= j
    return count

# Loop through each number from 1 to t (inclusive)
for i in range(1, t + 1):
    # Calculate the number of unique prime factors
    if unique_prime_factors_count(i) == 2:
        # Increment the count of prime numbers found
        prime_count += 1

# After checking all numbers, output the total count of prime numbers found
print(prime_count)
