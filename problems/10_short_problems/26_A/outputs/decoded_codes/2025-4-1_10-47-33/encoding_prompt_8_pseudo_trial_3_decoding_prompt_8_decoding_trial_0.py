def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_semiprimes(t):
    semiprime_count = 0

    for i in range(1, t + 1):
        distinct_prime_count = 0
        current_number = i

        for j in range(2, current_number):
            if current_number % j == 0 and is_prime(j):
                distinct_prime_count += 1

                while current_number % j == 0:
                    current_number //= j

        if distinct_prime_count == 2:
            semiprime_count += 1

    print(semiprime_count)

t = int(input())
count_semiprimes(t)
