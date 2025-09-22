# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to count semi-prime numbers up to a given limit
def count_semi_primes(t):
    result = 0  # Initialize the counter for semi-prime numbers

    # For each integer i from 1 to t (inclusive)
    for i in range(1, t + 1):
        count_divisors = 0  # Count distinct prime factors of i
        current_number = i   # Manipulate during factorization

        # Check for prime factors
        for j in range(2, i):  # Check divisors from 2 to i-1
            if current_number % j == 0 and is_prime(j):  # Check if j is a prime factor
                count_divisors += 1  # Found a new prime factor
                # Remove all instances of j from current_number
                while current_number % j == 0:
                    current_number //= j

        # If the number of distinct prime factors is equal to 2, it's a semi-prime
        if count_divisors == 2:
            result += 1  # Increment the semi-prime count

    return result  # Return the total count of semi-prime numbers found

# Input section
t = int(input())  # Read the upper limit from the user
# Call the function and print the result
print(count_semi_primes(t))
