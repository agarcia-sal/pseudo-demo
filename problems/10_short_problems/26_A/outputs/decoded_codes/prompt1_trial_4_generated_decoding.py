# 1. Start
# 2. Input the number of test cases t
t = int(input())

# 3. Initialize a variable result to 0
result = 0

# 4. For each number i from 1 to t do the following
for i in range(1, t + 1):
    # Initialize a variable count to 0
    count = 0
    # Set a variable number equal to i
    number = i
    
    # For each number j from 2 to i-1 do the following
    for j in range(2, i):
        # Check if number is divisible by j
        if number % j == 0:
            # If true, increment count by 1
            count += 1
            
            # While number is divisible by j, do the following
            while number % j == 0:
                # Divide number by j
                number //= j
                
    # After examining all potential factors, check if count is equal to 2
    if count == 2:
        # If true, increment result by 1
        result += 1

# 5. Output the value of result
print(result)

# 6. End
