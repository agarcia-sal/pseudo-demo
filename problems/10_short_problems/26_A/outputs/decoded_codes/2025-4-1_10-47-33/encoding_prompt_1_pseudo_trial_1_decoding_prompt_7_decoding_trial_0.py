# Define a function to count prime numbers up to a given integer
def count_primes():
    # Step 1: Read the upper limit for checking prime numbers
    t = int(input())
    
    # Step 2: Initialize the variable to store the total number of prime numbers found
    primeCount = 0
    
    # Step 3: Loop through each integer from 1 to t (inclusive)
    for i in range(1, t + 1):
        divisorCount = 0         # Initialize the count of divisors for the current number
        currentNumber = i        # Set the current number to i
        
        # Step 4: Check for divisors from 2 up to but not including i
        for j in range(2, i):
            if currentNumber % j == 0:  # If currentNumber is divisible by j
                divisorCount += 1        # Increment the divisor count
                # While loop to remove all factors of j from currentNumber
                while currentNumber % j == 0:
                    currentNumber //= j  # Divide currentNumber by j
        
        # Step 5: Determine if the current number is a prime
        # A prime number has exactly two distinct divisors: 1 and itself
        if divisorCount == 2:
            primeCount += 1  # Increment the prime count as i is prime

    # Step 6: Output the total number of prime numbers found
    print(primeCount)

# Run the function to execute the prime counting logic
count_primes()
