# Get Input
user_input = input()
absolute_input = abs(int(user_input))

# Initialize Variables
current_integer = 0 

# Loop for Triangular Numbers
while True:
    triangular_number = (current_integer * (current_integer + 1)) // 2
    difference = triangular_number - absolute_input

    # Check Conditions
    if triangular_number == absolute_input:
        print(current_integer)
        break
    elif triangular_number > absolute_input:
        if difference % 2 == 0:
            print(current_integer)
            break
            
    current_integer += 1
