# Step 1: Read integer input as `t`
t = int(input())

# Step 2: Initialize a variable `result` to 0
result = 0

# Step 3: FOR each integer `i` from 1 to `t` (inclusive)
for i in range(1, t + 1):
    # Step 3a: Initialize a variable `count` to 0
    count = 0
    # Step 3b: Set `number` to `i`
    number = i
    
    # Step 4: FOR each integer `j` from 2 to `i-1`
    for j in range(2, i):
        # Step 4a: IF `number` is divisible by `j`
        if number % j == 0:
            # Step 4ai: Increment `count` by 1
            count += 1
            # Step 4aii: WHILE `number` is divisible by `j`
            while number % j == 0:
                # Divide `number` by `j`
                number //= j

    # Step 5: IF `count` is equal to 2 THEN
    if count == 2:
        # Step 5a: Increment `result` by 1
        result += 1

# Step 6: Output `result`
print(result)
