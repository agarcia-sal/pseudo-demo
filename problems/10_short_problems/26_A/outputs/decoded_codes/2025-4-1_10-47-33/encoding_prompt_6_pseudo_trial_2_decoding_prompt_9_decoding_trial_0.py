# Start by reading an integer input called "totalNumbers".
total_numbers = int(input())

# Initialize a variable "countOfSpecialNumbers" to 0.
count_of_special_numbers = 0

# Loop through each integer "currentNumber" from 1 to "totalNumbers" (inclusive):
for current_number in range(1, total_numbers + 1):
    # Initialize a variable "divisorCount" to 0.
    divisor_count = 0
    # Set "currentValue" to "currentNumber".
    current_value = current_number

    # Loop through each integer "divisor" from 2 to "currentNumber - 1":
    for divisor in range(2, current_number):
        # If "currentValue" is divisible by "divisor":
        if current_value % divisor == 0:
            # Increment "divisorCount" by 1.
            divisor_count += 1
            # While "currentValue" is still divisible by "divisor":
            while current_value % divisor == 0:
                # Divide "currentValue" by "divisor".
                current_value //= divisor

    # If "divisorCount" is equal to 2:
    if divisor_count == 2:
        # Increment "countOfSpecialNumbers" by 1.
        count_of_special_numbers += 1

# After checking all numbers, print "countOfSpecialNumbers".
print(count_of_special_numbers)
