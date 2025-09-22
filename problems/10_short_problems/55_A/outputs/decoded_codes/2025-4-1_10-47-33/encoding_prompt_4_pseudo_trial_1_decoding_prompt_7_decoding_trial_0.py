# Start of the program

# Read input
n = int(input())  # Read the integer value for n

# Initialize a list to track boolean values
isPrime = [True] * n  # Create a list of size n, initialized to True
j = 0  # Initialize index j
i = 1  # Initialize counter i

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
remainingPrimes = [value for value in isPrime if value]  # List comprehension to filter True values

# Check if there are any remaining prime positions
if len(remainingPrimes) == 0:
    print('YES')  # No prime positions remaining
else:
    print('NO')   # There are remaining prime positions

# End of the program
