# Start by reading an integer value, t
t = int(input())

# Initialize a variable result to 0
result = 0

# For each integer i from 1 to t (inclusive)
for i in range(1, t + 1):
    # Initialize a variable count to 0
    count = 0
    # Set a temporary variable number to i for factorization
    number = i
    
    # For each integer j from 2 to one less than i
    for j in range(2, i):
        # If number is divisible by j
        if number % j == 0:
            # Increment the count of distinct prime factors by 1
            count += 1
            # While number is still divisible by j
            while number % j == 0:
                # Divide number by j to remove that factor completely
                number //= j
    
    # If count equals 2
    if count == 2:
        # Increment the result by 1
        result += 1

# After finishing the loop, print the value of result
print(result)


     def count_distinct_prime_factors(n):
         count = 0
         number = n
         for j in range(2, n):
             if number % j == 0:
                 count += 1
                 while number % j == 0:
                     number //= j
         return count

     # Main execution loop
     for i in range(1, t + 1):
         if count_distinct_prime_factors(i) == 2:
             result += 1
     