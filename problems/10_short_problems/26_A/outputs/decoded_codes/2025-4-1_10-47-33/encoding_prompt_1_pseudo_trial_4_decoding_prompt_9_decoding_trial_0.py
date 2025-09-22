# Read the upper limit of numbers to analyze
t = int(input())

# Initialize the result variable to count numbers with exactly two distinct prime factors
result = 0

# Loop through each integer from 1 to t (inclusive)
for i in range(1, t + 1):
    # Initialize a count of distinct prime factors for the current integer i
    count = 0
    currentNumber = i  # Set the current number to the integer we are analyzing

    # Check for factors from 2 up to one less than currentNumber
    for j in range(2, i):
        # If currentNumber is divisible by j, it is a prime factor
        if currentNumber % j == 0:
            count += 1  # We found a new distinct prime factor
            # Remove all occurrences of this prime factor
            while currentNumber % j == 0:
                currentNumber //= j  # Use integer division to divide

    # Check if we found exactly two distinct prime factors
    if count == 2:
        result += 1  # Count this number as it meets the criterion

# Display the final result
print(result)
