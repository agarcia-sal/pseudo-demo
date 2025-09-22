# Function to count numbers with exactly two unique prime factors
def count_special_numbers():
    # Read the total number of integers to consider
    total_numbers = int(input())
    # Initialize the count of special numbers
    count_of_special_numbers = 0

    # Loop through each integer from 1 to total_numbers (inclusive)
    for current_number in range(1, total_numbers + 1):
        # Track the number of unique divisors (prime factors)
        divisor_count = 0
        current_value = current_number

        # Check divisors from 2 up to current_number - 1
        for divisor in range(2, current_number):
            # Check if current value is divisible by the divisor
            if current_value % divisor == 0:
                # Found a new unique divisor
                divisor_count += 1
                # Remove all instances of this divisor from current_value
                while current_value % divisor == 0:
                    current_value //= divisor

        # Check if we found exactly two unique prime factors
        if divisor_count == 2:
            count_of_special_numbers += 1

    # Print the final count of special numbers
    print(count_of_special_numbers)

# Example of how to call the function
count_special_numbers()
