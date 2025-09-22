# Step 1: Read an integer value t, which represents the upper limit for checking numbers
t = int(input())

# Step 2: Initialize result to count numbers with exactly two distinct prime factors
result = 0

# Step 3: Loop through each integer i from 1 to t (inclusive)
for i in range(1, t + 1):
    # Step 4: Initialize count to 0 for distinct prime factors
    count = 0
    # Step 5: Set a temporary variable number to i for factorization
    number = i
    
    # Step 6: Check for prime factors from 2 to just less than i
    for j in range(2, i):
        # Step 7: If number is divisible by j
        if number % j == 0:
            # Increment count for distinct prime factors
            count += 1
            
            # Step 8: While number is still divisible by j
            while number % j == 0:
                # Divide number by j to remove that factor completely
                number //= j
    
    # Step 9: If count equals 2, then i has exactly two distinct prime factors
    if count == 2:
        # Increment result by 1 to account for this number
        result += 1

# Step 10: After finishing the loop, print the result
print(result)
