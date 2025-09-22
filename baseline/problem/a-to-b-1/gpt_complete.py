def modexp(a, b, MOD):
    res = 1
    while b != 0:
        if b % 2 == 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b //= 2  # Integer division
    return res

# Read input for n
n = int(input())
MOD = 10**9 + 7  # Define modulo value
# Read input for list A
A = list(map(int, input().split()))

product = 1
zero_indices = []  # Initialize list to track indices of zeros in A

# Calculate the product of non-zero elements in A
for i in range(n):
    if A[i] == 0:
        zero_indices.append(i)  # Store index of zero
    else:
        product = (product * A[i]) % MOD

# Read input for q
q = int(input())

# Process each query
for _ in range(q):
    # Read input for p
    p = list(map(int, input().split()))
    
    if p[0] == 0:  # Update operation
        if A[p[1] - 1] != 0:  # If the original value is non-zero
            product = (product * modexp(A[p[1] - 1], MOD - 2, MOD)) % MOD
            A[p[1] - 1] = p[2]
            if p[2] == 0:
                zero_indices.append(p[1] - 1)  # Add index to zero list
            else:
                product = (product * p[2]) % MOD
        else:  # If the original value is zero
            A[p[1] - 1] = p[2]
            if p[2] != 0:
                # No action for zero
                pass
            else:
                product = (product * p[2]) % MOD
                zero_indices.remove(p[1] - 1)  # Remove index from zero list if it was zero

    else:  # Query operation
        if A[p[1] - 1] != 0 and not zero_indices:
            ans = (product * modexp(A[p[1] - 1], MOD - 2, MOD)) % MOD
            print(ans)
        elif A[p[1] - 1] != 0 and zero_indices:
            print(0)
        elif A[p[1] - 1] == 0 and len(zero_indices) == 1:
            print(product % MOD)
        else:
            print(0)
