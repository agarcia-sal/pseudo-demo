# Start of the program

# Read input
n = int(input())

# Initialize a list to track boolean values
is_prime = [True] * n  # List of size n, all set to True
j = 0  # Index for the is_prime list
i = 1  # Counter, starting at 1

# Loop until counter exceeds 500000
while i <= 500000:
    # If the current index is marked as true in is_prime
    if is_prime[j]:
        # Mark the current index as false
        is_prime[j] = False
    
    # Increment the counter
    i += 1
    
    # Update the index using modulo to wrap around
    j = (j + i) % n

# Create a new list with only true values from is_prime
remaining_primes = [value for value in is_prime if value]

# Check if there are any remaining prime positions
if len(remaining_primes) == 0:
    print('YES')  # No prime positions remaining
else:
    print('NO')   # There are remaining prime positions

# End of the program
