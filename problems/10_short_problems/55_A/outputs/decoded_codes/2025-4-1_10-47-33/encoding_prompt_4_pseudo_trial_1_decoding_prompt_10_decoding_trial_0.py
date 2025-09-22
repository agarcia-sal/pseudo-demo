def main():
    # Read the size of the list from input
    n = int(input())
    
    # Initialize a list to track boolean values for primality
    is_prime = [True] * n
    
    j = 0  # Index for the is_prime list
    i = 1  # Counter
    
    # Loop until the counter exceeds 500000
    while i <= 500000:
        # If the current index is marked as true
        if is_prime[j]:
            # Mark the current index as false (not prime)
            is_prime[j] = False
        
        # Increment the counter
        i += 1
        
        # Update the index using modulo to wrap around
        j = (j + i) % n
    
    # Create a new list with only values that are True from is_prime
    remaining_primes = [value for value in is_prime if value]

    # Check if there are any remaining prime positions
    if len(remaining_primes) == 0:
        print('YES')  # No prime positions remaining
    else:
        print('NO')   # There are remaining prime positions

if __name__ == "__main__":
    main()
