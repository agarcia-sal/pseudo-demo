# Start of the program

# Step 1: Declare variable t as Integer
t = int(input())  # Input t from the User

# Step 4: Initialize res to 0 (This will hold the count of prime numbers)
res = 0

# Step 5: Loop from i = 1 to t (Inclusive)
for i in range(1, t + 1):
    cnt = 0  # Step 5.1: Initialize cnt to 0 (Count of distinct prime factors)
    num = i  # Step 5.2: Set num to i

    # Step 5.3: Loop from j = 2 to i - 1
    for j in range(2, i):
        if num % j == 0:  # Step 5.3.1: If j is a factor of num
            cnt += 1  # Step 5.3.1.1: Increment cnt by 1 (Count the factor)
            while num % j == 0:  # Step 5.3.1.2: While j is a factor
                num //= j  # Divide num by j (Remove the factor)

    # Step 5.4: If cnt equals 2 (i has exactly two distinct prime factors)
    if cnt == 2:
        res += 1  # Step 5.4.1: Increment res by 1 (Count this number as prime)

# Step 6: Output res (Total count of prime numbers)
print(res)  # Printing the total count of prime numbers

# End of the program
