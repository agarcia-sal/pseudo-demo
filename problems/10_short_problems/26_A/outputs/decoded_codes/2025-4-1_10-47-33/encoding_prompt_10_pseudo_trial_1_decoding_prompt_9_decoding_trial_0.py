# Step 1: Declare and initialize variables
t = 0            # Number of test cases
res = 0          # Result count of numbers with exactly two prime factors

# Step 2: Input number of test cases
t = int(input())  # Read number of test cases

# Step 3: Loop through each number from 1 to t
for i in range(1, t + 1):
    cnt = 0           # Count of distinct prime factors
    num = i           # Current number to check for factors

    # Step 4: Check for factors of the current number
    for j in range(2, i):
        if num % j == 0:  # If 'j' is a factor
            cnt += 1      # Increment the count of factors
            
            # Step 5: Divide num by j as long as it's divisible
            while num % j == 0:
                num //= j  # Reduce num by dividing it by j
            
    # Step 6: Check if the number has exactly two distinct prime factors
    if cnt == 2:
        res += 1  # Increment the result count

# Step 7: Output the result
print(res)
