def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for j in range(2, int(num**0.5) + 1):
        if num % j == 0:
            return False
    return True

def count_prime_numbers():
    # Step 1: Read number of test cases
    t = int(input())
    
    # Step 2: Initialize count of prime numbers
    res = 0
    
    # Step 3: Loop through each number from 1 to t
    for i in range(1, t + 1):
        # Step 4 & 5: Check if the current number is prime
        if is_prime(i):
            res += 1
            
    # Step 6: Output the total count of prime numbers found
    print(res)

# Call the function to execute the program
count_prime_numbers()
