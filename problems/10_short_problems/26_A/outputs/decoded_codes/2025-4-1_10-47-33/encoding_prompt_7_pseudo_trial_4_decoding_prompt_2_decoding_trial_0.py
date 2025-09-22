def count_semi_prime_numbers(input_number):
    result = 0
    
    for i in range(1, input_number + 1):
        prime_factor_count = 0
        current_number = i
        
        for j in range(2, current_number):
            if current_number % j == 0:  # Check if j is a prime factor
                prime_factor_count += 1
                
                # Divide current_number by j until it is no longer divisible
                while current_number % j == 0:
                    current_number //= j
        
        # Check if there are exactly 2 prime factors
        if prime_factor_count == 2:
            result += 1
            
    return result
