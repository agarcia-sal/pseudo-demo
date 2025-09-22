# Read an integer value for the upper limit
t = int(input())

# Initialize a variable to count the numbers with exactly two distinct prime factors
result = 0

# Loop through each integer from 1 to t (inclusive)
for i in range(1, t + 1):
    # Initialize a count of distinct prime factors for the current number i
    count = 0
    # Set a temporary variable for factorization
    number = i
    
    # Check for factors starting from 2 up to i-1
    for j in range(2, i):
        # If j is a prime factor of number
        if number % j == 0:
            count += 1  # Increment the count of distinct prime factors
            # While number is divisible by j, divide it completely by j
            while number % j == 0:
                number //= j  # Use integer division to remove the factor completely
    
    # If the count of distinct prime factors is exactly 2
    if count == 2:
        result += 1  # Increment the result count

# Print the final count of numbers with exactly two distinct prime factors
print(result)
