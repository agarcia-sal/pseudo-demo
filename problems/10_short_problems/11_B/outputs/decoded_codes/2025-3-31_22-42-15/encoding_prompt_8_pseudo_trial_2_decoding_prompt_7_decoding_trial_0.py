# Get Input
# Read a number from the user and convert it to an integer
input_number = int(input())
# Take the absolute value of the input number
absolute_input = abs(input_number)

# Initialize Variables
# Set a counter variable to keep track of the current integer
current_integer = 0

# Loop for Triangular Numbers
while True:
    # Calculate the triangular number for the current integer
    triangular_number = (current_integer * (current_integer + 1)) // 2
    
    # Calculate the difference between the triangular number and the absolute input value
    difference = triangular_number - absolute_input

    # Check Conditions
    if triangular_number == absolute_input:
        # If triangular number equals absolute input, display current integer and stop
        print(current_integer)
        break
    elif triangular_number > absolute_input:
        # If triangular number is greater than absolute input
        if difference % 2 == 0:
            # If the difference is even, display current integer and stop
            print(current_integer)
            break
    
    # Increment current_integer by 1 for the next iteration
    current_integer += 1
