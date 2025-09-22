# Function to calculate the absolute value of an integer
def absolute_value(x):
    return abs(x)

# Read an integer input and get its absolute value
absolute_value_input = absolute_value(int(input()))

# Initialize a counter variable
counter = 0

# Loop indefinitely until a break condition is met
while True:
    # Calculate the sum of the first 'counter' integers using the formula
    current_sum = (counter * (counter + 1)) // 2
    
    # Calculate the difference between current_sum and absolute_value_input
    difference = current_sum - absolute_value_input
    
    # Check if current_sum equals the absolute_value_input
    if current_sum == absolute_value_input:
        print(counter)  # Output the counter value
        break  # Exit the loop

    # Check if current_sum exceeds the absolute_value_input
    elif current_sum > absolute_value_input:
        # Check if the difference is even
        if difference % 2 == 0:
            print(counter)  # Output the counter value
            break  # Exit the loop
    
    # Increment the counter for the next iteration
    counter += 1
