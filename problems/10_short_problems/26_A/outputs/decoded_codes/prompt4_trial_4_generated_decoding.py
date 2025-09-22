def count_special_numbers():
    # Read the number of test cases (upper limit)
    t = int(input())

    # Initialize the count of special numbers
    count_of_special_numbers = 0

    # Loop through each number from 1 to t
    for i in range(1, t + 1):
        # Initialize the count of distinct prime factors
        distinct_prime_factors_count = 0
        
        # Assign the current number to num for factorization
        num = i
        
        # Loop through potential factors from 2 to i-1
        for j in range(2, i):
            # Check if j is a factor of num
            if num % j == 0:
                distinct_prime_factors_count += 1
                
                # While j is a factor of num, divide num by j
                while num % j == 0:
                    num //= j

        # Check if the number has exactly two distinct prime factors
        if distinct_prime_factors_count == 2:
            count_of_special_numbers += 1

    # Output the total count of special numbers
    print(count_of_special_numbers)

# Call the function to execute
count_special_numbers()
