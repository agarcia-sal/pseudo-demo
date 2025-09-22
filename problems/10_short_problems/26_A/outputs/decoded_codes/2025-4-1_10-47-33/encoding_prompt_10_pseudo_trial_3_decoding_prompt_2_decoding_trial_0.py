# Start Program
# Declare Variable `t` as Integer
t = int(input())  # Input `t` from the User

# Initialize `res` to 0 (This will hold the count of prime numbers)
res = 0

# Loop from `i = 1` to `t` (Inclusive)
for i in range(1, t + 1):
    # Initialize `cnt` to 0 (This will count factors of `i`)
    cnt = 0
    # Set `num` to `i` (This will be modified to find prime factors)
    num = i

    # Loop from `j = 2` to `i - 1`
    for j in range(2, i):
        # If `num modulo j equals 0` (j is a factor of num)
        if num % j == 0:
            # Increment `cnt` by 1 (Count the factor)
            cnt += 1
            # While `num modulo j equals 0`
            while num % j == 0:
                # Divide `num` by `j` (Remove the factor from num)
                num //= j

    # If `cnt equals 2` (i has exactly two distinct prime factors)
    if cnt == 2:
        # Increment `res` by 1 (Count this number as prime)
        res += 1

# Output `res` (Total count of prime numbers)
print(res)  # End Program
