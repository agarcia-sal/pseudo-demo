def main():
    # Step 1: Gather input
    first_input = input()
    second_input = input()
    
    # Step 2: Split input into individual components
    first_input_components = first_input.split()
    second_input_components = second_input.split()
    
    # Step 3: Initialize a counter for differences
    difference_counter = 0
    
    # Step 4: Compare corresponding components from both inputs
    for index in range(3):  # Compare the first three components (0 to 2 inclusive)
        first_value = int(first_input_components[index])
        second_value = int(second_input_components[index])
        
        # If the values are not equal, increment the difference counter
        if first_value != second_value:
            difference_counter += 1
    
    # Step 5: Determine and output the result based on the number of differences
    if difference_counter < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
