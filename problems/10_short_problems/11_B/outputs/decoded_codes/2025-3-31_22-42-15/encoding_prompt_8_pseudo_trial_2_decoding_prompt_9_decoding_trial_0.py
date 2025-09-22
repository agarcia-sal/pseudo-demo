# Read a number from the user and take its absolute value
input_value = int(input())
absolute_input = abs(input_value)

# Initialize a counter variable for the current integer
current_integer = 0

# Loop indefinitely to find the required triangular number
while True:
    # Calculate the triangular number for the current integer
    triangular_number = (current_integer * (current_integer + 1)) // 2
    
    # Calculate the difference between the triangular number and the absolute input value
    difference = triangular_number - absolute_input

    # Check if the triangular number is exactly equal to the absolute input value
    if triangular_number == absolute_input:
        print(current_integer)  # Display the current integer
        break  # Stop the loop
    
    # Check if the triangular number is greater than the absolute input value
    elif triangular_number > absolute_input:
        # Check if the difference is even
        if difference % 2 == 0:
            print(current_integer)  # Display the current integer
            break  # Stop the loop
    
    # Increment the current integer for the next iteration
    current_integer += 1
