# Start Program

# Declare variable `t` as an integer
t = int(input())  # Input t from the user

# Initialize res to 0 (this will hold the count of prime numbers)
res = 0  

# Loop from i = 1 to t (inclusive)
for i in range(1, t + 1):
    cnt = 0  # Initialize cnt to 0 (this will count distinct factors of i)
    num = i  # Set num to i (this will be modified to find prime factors)
    
    # Loop from j = 2 to i - 1
    for j in range(2, i):
        # If num modulo j equals 0 (j is a factor of num)
        if num % j == 0:
            cnt += 1  # Increment cnt by 1
            
            # While num modulo j equals 0:
            while num % j == 0:
                num //= j  # Divide num by j (remove the factor from num)
    
    # If cnt equals 1 (i has exactly one distinct prime factor, which is itself):
    if cnt == 1 and i > 1:  
        res += 1  # Increment res by 1 (count this number as prime)

# Output res (total count of prime numbers)
print(res) 

# End Program
