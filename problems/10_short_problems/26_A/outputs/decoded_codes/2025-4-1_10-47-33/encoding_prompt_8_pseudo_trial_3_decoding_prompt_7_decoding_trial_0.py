# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to count semiprimes up to a given number t
def count_semiprimes():
    # Get the input value for t
    t = int(input())
    
    # Initialize a variable to keep track of the count of semiprimes
    semiprime_count = 0
    
    # Loop through each number from 1 to t
    for i in range(1, t + 1):
        # Initialize a count for the number of distinct prime factors
        distinct_prime_count = 0
        # Copy the current number to a temporary variable for manipulation
        current_number = i

        # Check for factors starting from 2
        for j in range(2, i):
            # If j is a factor of current_number
            if current_number % j == 0:
                # Increment the count of distinct prime factors
                distinct_prime_count += 1
                
                # Continue dividing current_number by j until it no longer divides evenly
                while current_number % j == 0:
                    current_number //= j

        # After checking all possible factors
        # If the number has exactly two distinct prime factors, it is a semiprime
        if distinct_prime_count == 2:
            semiprime_count += 1

    # Output the total count of semiprimes found
    print(semiprime_count)

# Call the function to execute
count_semiprimes()
