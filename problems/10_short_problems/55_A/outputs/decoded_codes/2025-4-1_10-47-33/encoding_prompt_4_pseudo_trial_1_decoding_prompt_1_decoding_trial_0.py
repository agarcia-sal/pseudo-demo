# START

# Read input
n = int(input())  # n as an integer

# Initialize a list to track boolean values
isPrime = [True] * n  # list of size n, all set to True
j = 0  # Initialize index j to 0
i = 1  # Initialize counter i to 1

# Loop until counter exceeds 500000
while i <= 500000:
    # If the current index is marked as true
    if isPrime[j]:
        # Mark the current index as false
        isPrime[j] = False

    # Increment the counter
    i += 1

    # Update the index using modulo to wrap around
    j = (j + i) % n

# Create a new list with only true values from isPrime
remainingPrimes = [value for value in isPrime if value]

# Check if there are any remaining prime positions
if len(remainingPrimes) == 0:
    print('YES')  # No prime positions remaining
else:
    print('NO')  # There are remaining prime positions 

# END
