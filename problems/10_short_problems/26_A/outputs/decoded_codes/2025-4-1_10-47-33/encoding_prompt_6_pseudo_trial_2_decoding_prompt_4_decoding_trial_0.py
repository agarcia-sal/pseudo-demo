# Read the total number of integers to evaluate
total_numbers = int(input())

# Initialize a variable to count the numbers with exactly two distinct prime factors
count_of_special_numbers = 0

# Loop through each number from 1 to total_numbers (inclusive)
for current_number in range(1, total_numbers + 1):
    divisor_count = 0  # To keep track of the number of unique divisors for the current number
    current_value = current_number  # Set current value to the current number

    # Find divisors starting from 2 up to current_number - 1
    for divisor in range(2, current_number):
        if current_value % divisor == 0:  # If the current value is divisible by the divisor
            divisor_count += 1  # Increment the divisor count
            # Remove all instances of this divisor from current_value
            while current_value % divisor == 0:
                current_value //= divisor

    # If we found exactly 2 unique divisors, it's a special number
    if divisor_count == 2:
        count_of_special_numbers += 1  # Increment the count of special numbers

# After checking all numbers, print the count of special numbers
print(count_of_special_numbers)
