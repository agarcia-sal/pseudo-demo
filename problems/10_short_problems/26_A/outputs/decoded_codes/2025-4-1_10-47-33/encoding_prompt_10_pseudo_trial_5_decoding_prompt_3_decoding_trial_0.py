def count_prime_numbers():
    # Step 1: Read the number of test cases from user input
    t = int(input())
    
    # Step 2: Initialize a variable to count the prime numbers found
    prime_count = 0

    # Step 3: Loop through each number from 1 to t
    for i in range(2, t + 1):  # Start from 2, as 1 is not a prime number
        cnt = 0  # Counter for the number of distinct factors
        num = i  # Current number to check for primality

        # Step 4: Check for factors of num
        for j in range(2, int(num ** 0.5) + 1):  # Check up to the square root of num
            if num % j == 0:  # If j is a factor of num
                cnt += 1  # Increment the counter
                while num % j == 0:  # Remove all occurrences of j from num
                    num //= j

        # Step 5: Determine if i is a prime number
        if cnt == 1 and num > 1:  # A prime has exactly one distinct prime factor (itself)
            prime_count += 1  # Increment the prime count

    # Step 6: Output the total count of prime numbers found
    print(prime_count)

# Call the function to execute
count_prime_numbers()
