# Start the program
t = int(input())
result = 0

# For each integer 'i' from 1 to 't' (inclusive)
for i in range(1, t + 1):
    count = 0
    currentNumber = i

    # Check for unique prime factors
    for j in range(2, currentNumber):
        if currentNumber % j == 0:
            count += 1
            # Remove the factor completely
            while currentNumber % j == 0:
                currentNumber //= j

    # If count of unique prime factors is equal to 2
    if count == 2:
        result += 1

# Output the value of 'result'
print(result)
