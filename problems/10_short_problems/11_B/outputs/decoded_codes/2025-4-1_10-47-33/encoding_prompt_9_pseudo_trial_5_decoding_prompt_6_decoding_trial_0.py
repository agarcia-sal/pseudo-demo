# Receive and prepare input
target_number = int(input())  # Convert input to a non-negative integer

# Initialize variables
current_index = 0

# Process to find the desired index
while True:
    # Calculate the triangular number
    triangular_number = (current_index * (current_index + 1)) // 2
    
    # Calculate the difference
    difference = triangular_number - target_number
    
    # Check if triangular_number equals target_number
    if triangular_number == target_number:
        print(current_index)  # Output the answer
        break  # Exit the loop
    
    # Check if triangular_number is greater than target_number
    if triangular_number > target_number:
        # Check if the difference is even
        if difference % 2 == 0:
            print(current_index)  # Output the answer
            break  # Exit the loop
            
    # Increment current_index by 1 for the next iteration
    current_index += 1
