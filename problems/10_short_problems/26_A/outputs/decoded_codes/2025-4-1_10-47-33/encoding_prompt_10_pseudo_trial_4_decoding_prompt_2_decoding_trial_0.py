# Start Program

# Input Number of Test Cases
t = int(input())

# Initialize Result Counter
res = 0  # this will hold the count of prime numbers

# Loop Through Each Number from 1 to t
for i in range(1, t + 1):
    # Initialize counter for distinct prime factors
    cnt = 0  
    num = i  # to factorize current number

    # Loop to Find Factors
    for j in range(2, i):  # check factors from 2 to i-1
        if num % j == 0:  # if j is a factor of num
            cnt += 1  # found a new prime factor
            # While num is divisible by j
            while num % j == 0:
                num //= j  # remove the factor j from num

    # Check for Prime Condition
    if cnt == 2:  # check if the current number i has exactly two distinct prime factors
        res += 1  # count this number as valid

# Output Result
print(res)  # total count of numbers with exactly two distinct prime factors

# End Program
