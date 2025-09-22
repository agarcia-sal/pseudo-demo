# 1. Read integer input as `t`
t = int(input())

# 2. Initialize a variable `result` to 0
result = 0

# 3. FOR each integer `i` from 1 to `t` (inclusive)
for i in range(1, t + 1):
    # a. Initialize a variable `count` to 0
    count = 0
    # b. Set `number` to `i`
    number = i

    # 4. FOR each integer `j` from 2 to `i-1`
    for j in range(2, i):
        # a. IF `number` is divisible by `j`
        if number % j == 0:
            # i. Increment `count` by 1
            count += 1
            # ii. WHILE `number` is divisible by `j`
            while number % j == 0:
                # - Divide `number` by `j`
                number //= j

    # 5. IF `count` is equal to 2 THEN
    if count == 2:
        # a. Increment `result` by 1
        result += 1

# 6. Output `result`
print(result)
