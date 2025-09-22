# Get input from the user and convert it to its absolute value
number = abs(int(input()))

# Initialize a counter variable
index = 0

# Loop indefinitely until conditions are satisfied
while True:
    # Calculate the triangular number using the formula
    triangular_sum = (index * (index + 1)) // 2
    
    # Calculate the difference between triangular_sum and number
    difference = triangular_sum - number
    
    # Check if triangular_sum equals the input number
    if triangular_sum == number:
        print(index)  # number is a triangular number
        break  # exit the loop

    # Check if triangular_sum is greater than the input number
    elif triangular_sum > number:
        # If the difference is even
        if difference % 2 == 0:
            print(index)  # number can be represented as a triangular number with an adjustment
            break  # exit the loop
    
    # Increment the counter
    index += 1
