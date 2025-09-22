# Step 1: Initialize the variable for the number of test cases
t = int(input())

# Step 2: Initialize a variable to store the count of prime numbers
res = 0

# Step 3: Loop through each number from 1 to `t`
for i in range(1, t + 1):
    # Initialize a counter `cnt` to 0
    cnt = 0
    # Set variable `num` to `i`
    num = i
    
    # Step 4: Check for factors of `num`
    for j in range(2, i):
        if num % j == 0:
            # Increment `cnt` by 1
            cnt += 1
            # While `num` is divisible by `j`
            while num % j == 0:
                # Divide `num` by `j`
                num //= j
    
    # Step 5: Determine if `i` is a prime number
    if cnt == 2:
        # Increment `res` by 1
        res += 1

# Step 6: Output the total count of prime numbers found
print(res)
