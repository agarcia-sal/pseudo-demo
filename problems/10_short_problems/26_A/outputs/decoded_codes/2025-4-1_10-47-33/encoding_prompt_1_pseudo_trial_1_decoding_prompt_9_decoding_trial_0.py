# Function to count prime numbers up to a given integer
def count_primes():
    # Step 1: Input the upper limit for checking prime numbers
    t = int(input())  # Read an integer input
    
    # Step 2: Initialize result variable
    prime_count = 0  # This variable will store the total number of prime numbers found

    # Step 3: Loop through numbers from 1 to t (inclusive)
    for i in range(1, t + 1):
        divisor_count = 0  # Initialize divisor count for the current number
        current_number = i  # Set current number to i

        # Step 4: Check for divisors from 2 up to but not including i
        for j in range(2, i):
            if current_number % j == 0:  # If current number is divisible by j
                divisor_count += 1  # Increment divisor count
                # While current_number is divisible by j, reduce current_number
                while current_number % j == 0:
                    current_number //= j

        # Step 5: Determine if the number is prime
        if divisor_count == 1:  # A prime has exactly two distinct divisors: 1 and itself
            prime_count += 1  # Increment the prime count

    # Step 6: Output the total number of prime numbers found
    print(prime_count)

# Call the function to execute the code
count_primes()
