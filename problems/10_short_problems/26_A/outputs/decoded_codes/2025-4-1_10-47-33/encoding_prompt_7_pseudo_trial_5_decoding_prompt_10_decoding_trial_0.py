def count_semi_primes(input_number):
    result_counter = 0  # Initialize the count of semi-primes

    for current_number in range(1, input_number + 1):
        divisor_count = 0  # Reset divisor count for each current number
        temp_number = current_number  # Create a mutable version of current_number

        # Check potential divisors from 2 to current_number - 1
        for potential_divisor in range(2, current_number):
            if temp_number % potential_divisor == 0:  # Check for divisibility
                divisor_count += 1  # Increment divisor count

                # Divide temp_number by potential_divisor until it is not divisible
                while temp_number % potential_divisor == 0:
                    temp_number //= potential_divisor

        # If exactly two unique prime factors were found
        if divisor_count == 2:
            result_counter += 1  # Increment the semi-prime count

    return result_counter  # Return the total count of semi-primes


# Example usage
t = int(input())  # Read an integer input from the user
print(count_semi_primes(t))  # Call the function and print the result
