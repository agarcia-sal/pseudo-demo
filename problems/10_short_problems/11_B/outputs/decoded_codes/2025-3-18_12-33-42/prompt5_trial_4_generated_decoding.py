# Function to find the smallest non-negative integer that, when added to appropriate integers, equals the input number
def find_smallest_integer():
    # Step 1: Get user input and convert to absolute value
    input_number = abs(int(input()))
    
    # Step 2: Initialize the counter
    counter = 0
    
    # Step 3: Continue indefinitely until a condition is met
    while True:
        # Step 4: Calculate the sum of the first 'counter' integers
        sum_to_counter = (counter * (counter + 1)) / 2
        
        # Step 5: Calculate the difference
        difference = sum_to_counter - input_number
        
        # Step 6: Check conditions to determine output
        if sum_to_counter == input_number:
            # Found exact match, output the counter
            print(counter)
            break
        elif sum_to_counter > input_number:
            # Check if the difference is even
            if difference % 2 == 0:
                # Valid solution found, output the counter
                print(counter)
                break
        
        # Increment the counter for the next iteration
        counter += 1

# Call the function to execute the program
find_smallest_integer()
