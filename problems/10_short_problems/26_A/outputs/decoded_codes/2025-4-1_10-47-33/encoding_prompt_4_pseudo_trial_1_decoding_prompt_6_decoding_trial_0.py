# Read integer input as `t`
t = int(input())

# Initialize a variable `result` to 0
result = 0

# FOR each integer `i` from 1 to `t` (inclusive)
for i in range(1, t + 1):
    # Initialize a variable `count` to 0
    count = 0
    # Set `number` to `i`
    number = i
    
    # FOR each integer `j` from 2 to `i-1`
    for j in range(2, i):
        # IF `number` is divisible by `j`
        if number % j == 0:
            # Increment `count` by 1
            count += 1
            # WHILE `number` is divisible by `j`
            while number % j == 0:
                # Divide `number` by `j`
                number //= j
    
    # IF `count` is equal to 2 THEN
    if count == 2:
        # Increment `result` by 1
        result += 1

# Output `result`
print(result)
