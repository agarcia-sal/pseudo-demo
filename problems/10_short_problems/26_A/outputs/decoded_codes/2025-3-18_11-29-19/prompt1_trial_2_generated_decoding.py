# Start
# Read input: Get the integer value t that represents the upper limit.
t = int(input())

# Initialize a variable result to 0, which will store the count of specific numbers.
result = 0

# For each number i from 1 to t:
for i in range(1, t + 1):
    # Initialize a variable count to 0, which will keep track of the number of distinct prime factors of i.
    count = 0
    # Set currentNumber to i.
    currentNumber = i

    # For each potential factor j from 2 to (i - 1):
    for j in range(2, i):
        # If currentNumber is divisible by j:
        if currentNumber % j == 0:
            # Increment count by 1.
            count += 1
            # While currentNumber is divisible by j:
            while currentNumber % j == 0:
                # Divide currentNumber by j (to remove this factor completely).
                currentNumber //= j

    # If count is exactly 2:
    if count == 2:
        # Increment result by 1 (indicating that i has exactly two distinct prime factors).
        result += 1

# Output the value of result:
# This value represents the count of numbers from 1 to t that have exactly two distinct prime factors.
print(result)
# End
