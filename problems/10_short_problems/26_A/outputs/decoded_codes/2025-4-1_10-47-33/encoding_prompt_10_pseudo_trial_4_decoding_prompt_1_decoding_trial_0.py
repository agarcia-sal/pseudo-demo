# Start Program

# Input Number of Test Cases
t = int(input())

# Initialize Result Counter
res = 0  # this will hold the count of prime numbers

# Loop Through Each Number from 1 to t
for i in range(1, t + 1):  # Looping from 1 to t inclusive
    cnt = 0  # this will count the number of distinct prime factors
    num = i  # to factorize current number

    # Loop to Find Factors
    for j in range(2, i):  # Looping from 2 to i-1
        if num % j == 0:  # check if j is a factor of num
            cnt += 1  # found a new prime factor
            
            while num % j == 0:  # While num is divisible by j
                num //= j  # remove the factor j from num

    # Check for Prime Condition
    if cnt == 2:  # verifies that the current number i has exactly two distinct prime factors
        res += 1  # count this number as valid

# Output Result
print(res)  # total count of numbers with exactly two distinct prime factors

# End Program
