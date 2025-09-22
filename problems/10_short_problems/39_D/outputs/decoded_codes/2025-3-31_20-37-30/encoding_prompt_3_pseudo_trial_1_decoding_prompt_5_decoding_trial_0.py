def main():
    # Prompt user for two inputs
    first_input = input()
    second_input = input()
    
    # Split the inputs into lists of values
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Iterate over the first three elements of both lists
    for index in range(3):
        first_value = int(first_list[index])  # Convert first list values to integers
        second_value = int(second_list[index])  # Convert second list values to integers
        
        # Check if the current values are different
        if first_value != second_value:
            difference_count += 1  # Increment difference count
        
    # Decide the output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start program execution
main()
