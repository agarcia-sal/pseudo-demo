# Read input
n = int(input())  # Read an integer input and assign it to n

# Initialize a list to track boolean values
is_prime = [True] * n  # Create a list 'is_prime' of size n, all set to True
j = 0  # Initialize index j to 0
i = 1  # Initialize counter i to 1

# Loop until counter exceeds 500000
while i <= 500000:  # While i is less than or equal to 500000
    # If the current index is marked as true
    if is_prime[j]:  # If is_prime[j] is True
        # Mark the current index as false
        is_prime[j] = False  # Set is_prime[j] to False
    
    # Increment the counter
    i += 1  # Increment i by 1
    
    # Update the index using modulo to wrap around
    j = (j + i) % n  # Update j to (j + i) MOD n

# Create a new list with only true values from is_prime
remaining_primes = [value for value in is_prime if value]  # List comprehension to get all True values

# Check if there are any remaining prime positions
if len(remaining_primes) == 0:  # If the length of remaining_primes is 0
    print('YES')  # Print 'YES' if no prime positions remaining
else:
    print('NO')  # Print 'NO' if there are remaining prime positions
