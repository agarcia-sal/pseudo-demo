# Start Program

# Input Number of Test Cases
t = int(input())  # Read the number of test cases

# Initialize Result Counter
res = 0  # This variable will hold the count of numbers with exactly two distinct prime factors

# Loop Through Each Number from 1 to t
for i in range(1, t + 1):  # Loop through all integers from 1 to t
    cnt = 0  # Initialize a counter for distinct prime factors
    num = i  # Set num to the current integer to factorize it

    # Loop to Find Factors
    for j in range(2, i):  # Check for factors from 2 to i-1
        if num % j == 0:  # If j is a factor of num
            cnt += 1  # Increment the count of distinct prime factors
            # Continue dividing num by j until it is no longer divisible
            while num % j == 0:
                num //= j  # Remove the factor j from num

    # Check for Prime Condition
    if cnt == 2:  # If there are exactly two distinct prime factors
        res += 1  # Increment the result count

# Output Result
print(res)  # Print the total count of numbers with exactly two distinct prime factors

# End Program
