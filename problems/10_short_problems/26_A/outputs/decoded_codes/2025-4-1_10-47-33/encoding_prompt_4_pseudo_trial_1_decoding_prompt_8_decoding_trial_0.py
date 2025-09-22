t = int(input())
result = 0

for i in range(1, t + 1):
    count = 0
    number = i
    
    for j in range(2, i):
        if number % j == 0:
            count += 1
            while number % j == 0:
                number //= j
    
    if count == 2:
        result += 1

print(result)


def count_two_distinct_prime_factors(t):
    result = 0

    for i in range(2, t + 1):  # We start from 2 since 1 has no prime factors
        count = 0
        number = i
        
        for j in range(2, int(number**0.5) + 1):  # Check up to the square root of the number
            if number % j == 0:
                count += 1
                while number % j == 0:
                    number //= j
        
        if number > 1:  # If there's any prime factor greater than sqrt(number)
            count += 1
        
        if count == 2:
            result += 1

    return result

t = int(input())
print(count_two_distinct_prime_factors(t))
