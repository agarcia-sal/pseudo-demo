def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_semiprimes(t):
    semiprime_count = 0

    for current_number in range(1, t + 1):
        factor_count = 0
        temp_number = current_number

        for possible_prime in range(2, current_number):
            if temp_number % possible_prime == 0:
                factor_count += 1

                while temp_number % possible_prime == 0:
                    temp_number //= possible_prime

        if factor_count == 2:
            semiprime_count += 1

    print(semiprime_count)

# Main program
t = int(input())
count_semiprimes(t)
