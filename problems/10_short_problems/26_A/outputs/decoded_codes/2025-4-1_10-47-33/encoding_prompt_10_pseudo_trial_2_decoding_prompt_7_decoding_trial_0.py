# Step 1: Read the input value
t = int(input())  # Get the integer input from the user

# Step 2: Initialize result counter
res = 0

# Step 3: Loop through each integer from 1 to t
for i in range(1, t + 1):
    # Step 4: Initialize prime factor counter
    cnt = 0
    num = i  # Store current value of i in num

    # Step 5: Check for factors of num
    for j in range(2, i):
        if num % j == 0:  # Check if j is a factor of num
            # Increment count of prime factors
            cnt += 1
            
            # Step 6: Remove all occurrences of the factor j from num
            while num % j == 0:  # While j is a factor of num
                num //= j  # Divide num by j

    # Step 7: Check if the count of prime factors equals 2
    if cnt == 2:  # Check if there are exactly 2 prime factors
        # Step 8: Increment the result counter for each valid i
        res += 1  # Found a number with exactly 2 prime factors

# Step 9: Output the result
print(res)  # Print the final count of numbers with exactly 2 prime factors
