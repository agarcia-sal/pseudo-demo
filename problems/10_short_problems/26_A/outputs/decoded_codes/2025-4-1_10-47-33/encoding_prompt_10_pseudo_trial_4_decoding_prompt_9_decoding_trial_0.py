# Start Program

# Input Number of Test Cases
t = int(input())  # Number of test cases

# Initialize Result Counter
res = 0  # This will hold the count of numbers with exactly two distinct prime factors

# Loop Through Each Number from 1 to t
for i in range(1, t + 1):  # Looping through each integer from 1 to t
    cnt = 0  # Initialize counter for distinct prime factors
    num = i  # Set num to the current number i

    # Loop to Find Factors
    for j in range(2, i):  # Loop through possible factors from 2 to i-1
        if num % j == 0:  # Check if j is a factor of num
            cnt += 1  # Found a new distinct prime factor
            # Remove all instances of this factor from num
            while num % j == 0:
                num //= j  # Divide num by j until it no longer can be divided

    # Check for Prime Condition
    if cnt == 2:  # This verifies that i has exactly two distinct prime factors
        res += 1  # Count this number

# Output Result
print(res)  # Total count of numbers with exactly two distinct prime factors

# End Program
