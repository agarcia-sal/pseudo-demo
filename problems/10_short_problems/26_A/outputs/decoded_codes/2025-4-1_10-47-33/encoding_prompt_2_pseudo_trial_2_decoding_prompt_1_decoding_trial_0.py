# Start
t = int(input())  # Read an integer value, t

result = 0  # Initialize result to 0

# For each integer i from 1 to t (inclusive)
for i in range(1, t + 1):
    count = 0  # Initialize count to 0
    number = i  # Set temporary variable number to i for factorization
    
    # For each integer j from 2 to one less than i
    for j in range(2, i):
        if number % j == 0:  # If number is divisible by j
            count += 1  # Increment the count of distinct prime factors
            while number % j == 0:  # While number is still divisible by j
                number //= j  # Divide number by j to remove that factor completely

    # If count equals 2
    if count == 2:  
        result += 1  # Increment result by 1

# After finishing the loop
print(result)  # Print the value of result

# End
