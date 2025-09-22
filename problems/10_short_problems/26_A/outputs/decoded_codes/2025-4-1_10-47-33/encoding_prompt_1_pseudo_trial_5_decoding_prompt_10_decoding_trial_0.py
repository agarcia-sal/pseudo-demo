def count_numbers_with_two_distinct_prime_factors(limit):
    # Initialize result count to track numbers with exactly two distinct prime factors
    result_count = 0
    
    # Iterate through each number from 1 up to the provided limit
    for current_number in range(1, limit + 1):
        distinct_prime_factors_count = 0
        temp_number = current_number
        
        # Check each potential factor starting from 2 to current_number - 1
        for potential_factor in range(2, current_number):
            if temp_number % potential_factor == 0:  # Check if it's a factor
                distinct_prime_factors_count += 1  # Found a new distinct prime factor
                
                # Eliminate all occurrences of this prime factor
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor
            
            # If already two distinct factors found, we can break early
            if distinct_prime_factors_count > 2:
                break

        # After checking all potential factors, check the count for distinct prime factors
        if distinct_prime_factors_count == 2:
            result_count += 1

    return result_count

# Main execution
if __name__ == "__main__":
    t = int(input())  # Reading input for the upper limit
    result = count_numbers_with_two_distinct_prime_factors(t)
    print(result)  # Outputting the count
