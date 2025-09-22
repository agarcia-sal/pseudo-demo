# Function to check if a number is prime and count primes up to a given number t
def count_primes():
    # Step 1: Read the number of test cases from user input
    t = int(input())
    
    # Step 2: Initialize the count of prime numbers
    res = 0

    # Step 3: Loop through each number from 1 to t
    for i in range(1, t + 1):
        cnt = 0   # Counter for factors of num
        num = i   # The number to check for primality
        
        # Step 4: Check for factors of num
        for j in range(2, i):  # Check for factors from 2 to i-1
            if num % j == 0:   # If num is divisible by j
                cnt += 1       # Increment the factor count
                while num % j == 0:  # Remove all factors of j
                    num //= j
        
        # Step 5: Determine if i is a prime number
        if cnt == 1:  # A prime number should have exactly 1 factor (excluding 1)
            res += 1   # Increment prime count
            
    # Step 6: Print the total count of prime numbers found
    print(res)

# Call the function to execute
count_primes()
