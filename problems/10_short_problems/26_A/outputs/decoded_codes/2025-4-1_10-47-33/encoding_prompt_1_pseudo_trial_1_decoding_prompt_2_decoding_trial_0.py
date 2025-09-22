# Input: Read an integer t which represents the upper limit for checking prime numbers.
t = int(input())

# Initialize Result: Create a variable called primeCount and set it to 0.
primeCount = 0

# Loop Through Numbers: For each integer i from 1 to t (inclusive).
for i in range(1, t + 1):
    divisorCount = 0  # Initialize divisorCount to 0.
    currentNumber = i  # Set currentNumber to the value of i.

    # Check for Divisors: For each integer j starting from 2 up to but not including i.
    for j in range(2, i):
        if currentNumber % j == 0:  # If currentNumber is divisible by j.
            divisorCount += 1  # Increment divisorCount by 1.
            # While currentNumber is divisible by j, divide currentNumber by j.
            while currentNumber % j == 0:
                currentNumber //= j  # Update currentNumber by dividing it by j.

    # Determine Primality: After checking all possible divisors.
    if divisorCount == 1 and i > 1:  # Check if i has exactly 2 distinct divisors and ensure i > 1
        primeCount += 1  # Increment primeCount by 1 (as i is identified as a prime number).

# Output: After examining all numbers, print the value of primeCount.
print(primeCount)
