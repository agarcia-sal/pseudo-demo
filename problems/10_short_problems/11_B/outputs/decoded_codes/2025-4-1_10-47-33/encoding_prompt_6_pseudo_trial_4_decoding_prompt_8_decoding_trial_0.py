def abs_value(num):
    return abs(num)

def is_even(n):
    return n % 2 == 0

# Read the integer input and take its absolute value
absolute_value = abs_value(int(input()))

# Initialize the counter variable
counter = 0

# Loop indefinitely until a break condition is met
while True:
    # Calculate the sum of the first 'counter' integers
    current_sum = (counter * (counter + 1)) // 2

    # Calculate the difference between current_sum and absolute_value
    difference = current_sum - absolute_value

    # Check if the current_sum equals the absolute_value
    if current_sum == absolute_value:
        print(counter)  # Output the counter value
        break

    # Check if current_sum exceeds absolute_value
    elif current_sum > absolute_value:
        # Check if the difference is even
        if is_even(difference):
            print(counter)  # Output the counter value
            break

    # Increment the counter for the next iteration
    counter += 1
