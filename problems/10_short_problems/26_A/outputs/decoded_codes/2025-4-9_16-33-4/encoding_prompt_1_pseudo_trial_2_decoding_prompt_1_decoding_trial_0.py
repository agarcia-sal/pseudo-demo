# 1. Start Program

# 2. Get Input
tot = int(input())

# 3. Initialize Result Counter
pri = 0  # This will store the count of prime numbers.

# 4. Loop Through Each Number
for cur in range(1, tot + 1):
    # 1. Set Divisor Count
    dvc = 0  # This will count how many divisors 'cur' has.
    # 2. Set Working Number
    wor = cur

    # 3. Check for Divisibility
    for pot in range(2, cur):
        # If 'wor' is divisible by 'pot'
        if wor % pot == 0:
            # 1. Increase Divisor Count
            dvc += 1
            # 2. Divide Until Not Divisible
            while wor % pot == 0:
                wor //= pot  # Remove that prime factor.

    # 4. Check If Number is Prime
    if dvc == 2:  # It has exactly two distinct positive divisors.
        pri += 1  # Increment prime counter.

# 5. Output Result
print(pri)  # Print the total number of prime numbers found from 1 to 'tot'
