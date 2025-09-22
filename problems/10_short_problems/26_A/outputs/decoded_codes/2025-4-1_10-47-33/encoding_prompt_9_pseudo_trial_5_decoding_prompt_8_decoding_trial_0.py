def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_semiprimes(t):
    semiprime_count = 0
    
    for current_number in range(1, t + 1):
        prime_factor_count = 0
        divided_number = current_number
        
        for possible_factor in range(2, current_number):
            if divided_number % possible_factor == 0 and is_prime(possible_factor):
                prime_factor_count += 1
                while divided_number % possible_factor == 0:
                    divided_number //= possible_factor
            
            if prime_factor_count > 2:
                break
            
        if prime_factor_count == 2:
            semiprime_count += 1
            
    return semiprime_count

# Main block to run the function with user input
t = int(input())
result = count_semiprimes(t)
print(result)
