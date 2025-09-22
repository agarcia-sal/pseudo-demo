MOD = 10**9 + 7

def modexp(a, b):
    res = 1
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b //= 2
    return res

def main():
    n = int(input())
    A = list(map(int, input().split()))
    
    zero_indices = []  # Track indices of zeros
    product = 1

    # Calculate initial product and zero indices
    for i in range(n):
        if A[i] == 0:
            zero_indices.append(i)
        else:
            product = (product * A[i]) % MOD

    q = int(input())
    for _ in range(q):
        p = list(map(int, input().split()))
        if p[0] == 0:
            if A[p[1] - 1] != 0:
                product = (product * modexp(A[p[1] - 1], MOD - 2)) % MOD
            
            A[p[1] - 1] = p[2]
            
            if p[2] == 0:
                zero_indices.append(p[1] - 1)
            else:
                product = (product * p[2]) % MOD
                if (p[1] - 1) in zero_indices:
                    zero_indices.remove(p[1] - 1)
        else:
            if A[p[1] - 1] != 0 and not zero_indices:
                print((product * modexp(A[p[1] - 1], MOD - 2)) % MOD)
            else:
                print(0)

if __name__ == "__main__":
    main()
