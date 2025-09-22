# 1. Start Program

# 2. Get Input: 
tot = int(input())  # tot is an integer input from the user

# 3. Initialize Result Counter: 
pri = 0  # pri is initialized to 0 to count prime numbers

# 4. Loop Through Each Number:
for cur in range(1, tot + 1):  # cur iterates from 1 to tot (inclusive)
    # 1. Set Divisor Count:
    dvc = 0  # dvc counts the number of divisors of cur
    
    # 2. Set Working Number: 
    wor = cur  # wor is set to the current number cur

    # 3. Check for Divisibility:
    for pot in range(2, cur):  # pot checks potential divisors from 2 to cur-1
        if wor % pot == 0:  # If wor is divisible by pot
            # 1. Increase Divisor Count:
            dvc += 1  # Increment the divisor count
            # 2. Divide Until Not Divisible:
            while wor % pot == 0:  # While wor is divisible by pot
                wor //= pot  # Divide wor by pot to remove that prime factor

    # 4. Check If Number is Prime:
    if dvc == 2:  # If there are exactly two distinct divisors
        pri += 1  # Increment the prime number count

# 5. Output Result:
print(pri)  # Outputting the total number of prime numbers found from 1 to tot
