def check_differences_between_inputs():
    # Read two strings of space-separated integers from user input
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a variable to count differences
    difference_count = 0
    
    # Loop over the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the corresponding elements are different
        if first_value != second_value:
            # Increment the difference count
            difference_count += 1
            
    # Decision based on the number of differences counted
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Ensure the function runs only when the script is executed directly
if __name__ == "__main__":
    check_differences_between_inputs()
