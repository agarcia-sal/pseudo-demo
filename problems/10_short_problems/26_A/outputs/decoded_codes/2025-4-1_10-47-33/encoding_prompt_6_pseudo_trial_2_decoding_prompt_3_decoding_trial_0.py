def count_special_numbers():
    # Step 1: Read an integer input called "totalNumbers"
    total_numbers = int(input())
    
    # Step 2: Initialize a variable "countOfSpecialNumbers" to store the result
    count_of_special_numbers = 0

    # Step 3: Loop through each integer from 1 to "totalNumbers" (inclusive)
    for current_number in range(1, total_numbers + 1):
        # Initialize divisor count for the current number
        divisor_count = 0
        current_value = current_number

        # Step 3c: Loop through possible divisors
        for divisor in range(2, current_number):
            # Step 3c.i: Check if current_value is divisible by divisor
            if current_value % divisor == 0:
                divisor_count += 1
                
                # Step 3c.ii: Factor out the divisor completely
                while current_value % divisor == 0:
                    current_value //= divisor

        # Step 3d: Check for two unique divisors
        if divisor_count == 2:
            count_of_special_numbers += 1

    # Step 4: Print the final count of special numbers
    print(count_of_special_numbers)

# Call the function to execute
count_special_numbers()
