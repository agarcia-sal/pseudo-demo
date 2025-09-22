def main_process():
    # Step 1: Read two lines of input from the user
    first_input = input()
    second_input = input()
    
    # Step 2: Split the input strings into lists of values
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Step 3: Initialize a counter to keep track of differences
    difference_count = 0
    
    # Step 4: Compare the first three corresponding values from both lists
    for index in range(3):  # Loop over indices 0 to 2
        # Ensure the lists have enough elements
        if index < len(first_values) and index < len(second_values):
            value_a = int(first_values[index])  # Convert to integer
            value_b = int(second_values[index])  # Convert to integer
            
            # Step 5: If the values are different, increment the difference counter
            if value_a != value_b:
                difference_count += 1
    
    # Step 6: Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    main_process()
