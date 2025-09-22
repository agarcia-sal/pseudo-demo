# Get input from user and convert to an absolute integer value
target_number = abs(int(input()))

# Initialize the variable to hold the current integer
current_integer = 0

# Start an infinite loop to find the required integer
while True:
    # Calculate the sum of integers from 0 to current_integer
    sum_of_integers = current_integer * (current_integer + 1) // 2
    
    # Calculate the difference between sum_of_integers and target_number
    difference = sum_of_integers - target_number

    # Check if the sum_of_integers equals the target_number
    if sum_of_integers == target_number:
        # Output the current_integer if the condition is met
        print(current_integer)
        break
    
    # Check if sum_of_integers is greater than target_number
    if sum_of_integers > target_number:
        # Check if the difference is an even number
        if difference % 2 == 0:
            # Output the current_integer if the difference is even
            print(current_integer)
            break
    
    # Increment current_integer to check the next number
    current_integer += 1
