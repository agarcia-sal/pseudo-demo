def main():
    # Step 1: Read input
    n = int(input())
    
    # Step 2: Initialize a list to track boolean values
    is_prime = [True] * n  # Create a list of size n, all set to True
    j = 0  # Initialize index j
    i = 1  # Initialize counter i
    
    # Step 3: Loop until counter exceeds 500,000
    while i <= 500000:
        # If the current index is marked as true
        if is_prime[j]:
            # Mark the current index as false
            is_prime[j] = False
        
        # Increment the counter
        i += 1
        
        # Update the index using modulo to wrap around
        j = (j + i) % n
    
    # Step 4: Create a new list with only True values from is_prime
    remaining_primes = [value for value in is_prime if value]
    
    # Step 5: Check if there are any remaining prime positions
    if len(remaining_primes) == 0:
        print('YES')  # No prime positions remaining
    else:
        print('NO')  # There are remaining prime positions

# Execute the main function
if __name__ == "__main__":
    main()
