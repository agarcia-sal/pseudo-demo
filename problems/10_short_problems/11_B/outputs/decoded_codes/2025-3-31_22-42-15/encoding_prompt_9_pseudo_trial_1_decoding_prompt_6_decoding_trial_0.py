# Initialize absolute value and index
absolute_value = abs(int(input()))  # Read input as integer and take absolute value
index = 0  # This will be used to calculate triangular numbers

# Start an infinite loop
while True:
    # Calculate triangular number using the formula
    triangular_number = (index * (index + 1)) // 2  # Using integer division for exact result
    
    # Calculate the difference between triangular number and absolute value
    difference = triangular_number - absolute_value
    
    # Check for equality
    if triangular_number == absolute_value:
        print(index)  # Output index if triangular number equals the absolute value
        break  # Exit the loop
        
    # Check for when triangular number is greater than absolute value
    if triangular_number > absolute_value:
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # Output index if difference is even
            break  # Exit the loop
            
    # Increment index for the next triangular number calculation
    index += 1
