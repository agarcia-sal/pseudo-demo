# Step 1: Start by reading an integer value, t, which represents the upper limit for checking numbers.
t = int(input())

# Step 2: Initialize a variable result to 0.
result = 0

# Step 3: For each integer i from 1 to t (inclusive):
for i in range(1, t + 1):
    # Initialize a variable count to 0.
    count = 0
    # Set a temporary variable number to i for factorization.
    number = i
    
    # Step 3.5: For each integer j from 2 to one less than i.
    for j in range(2, i):
        # If number is divisible by j (j is a factor of number):
        if number % j == 0:
            # Increment the count of distinct prime factors by 1.
            count += 1
            
            # While number is still divisible by j:
            while number % j == 0:
                # Divide number by j to remove that factor completely.
                number //= j
    
    # Step 4: If count equals 2:
    if count == 2:
        # Increment result by 1 to account for this number.
        result += 1

# Step 5: After finishing the loop, print the value of result.
print(result)
