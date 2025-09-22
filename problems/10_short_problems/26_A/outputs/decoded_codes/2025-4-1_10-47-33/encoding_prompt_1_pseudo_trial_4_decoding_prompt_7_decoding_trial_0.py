# Start of the program to count numbers with exactly two distinct prime factors
# Read an integer value `t` from user input
t = int(input())

# Initialize a variable `result` to keep count of numbers with exactly two distinct prime factors
result = 0

# Loop through each integer `i` from 1 to `t` (inclusive)
for i in range(1, t + 1):
    count = 0  # Count of distinct prime factors for the current number `i`
    currentNumber = i  # Copy of `i` to manipulate for factorization

    # Check for potential prime factors from 2 to one less than `i`
    for j in range(2, i):
        if currentNumber % j == 0:  # If `j` is a factor of `currentNumber`
            count += 1  # We found a new prime factor
            
            # Remove all occurrences of the prime factor `j`
            while currentNumber % j == 0:
                currentNumber //= j

    # After checking factors, if we found exactly two distinct prime factors
    if count == 2:
        result += 1  # Increment the result count

# Display the result, which is the total count of integers with exactly two distinct prime factors
print(result)
