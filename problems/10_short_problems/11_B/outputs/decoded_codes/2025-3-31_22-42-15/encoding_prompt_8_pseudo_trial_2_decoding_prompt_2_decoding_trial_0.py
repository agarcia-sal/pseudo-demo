# Step 1: Get Input
number = int(input())  # Read a number from the user and convert to an integer
absolute_input = abs(number)  # Take the absolute value

# Step 2: Initialize Variables
current_integer = 0  # Set a counter variable

# Step 3: Loop for Triangular Numbers
while True:  # Repeat indefinitely
    # Calculate the triangular number
    triangular_number = (current_integer * (current_integer + 1)) // 2
    
    # Calculate the difference
    difference = triangular_number - absolute_input

    # Check Conditions
    if triangular_number == absolute_input:  # Exact match
        print(current_integer)  # Display the current integer
        break  # Stop the loop
    elif triangular_number > absolute_input:  # Triangular number exceeds the input
        if difference % 2 == 0:  # Check if difference is even
            print(current_integer)  # Display the current integer
            break  # Stop the loop
   
    # Increment current_integer
    current_integer += 1
