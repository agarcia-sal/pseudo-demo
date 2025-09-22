def do_main():
    # Get user input for two strings
    string_1 = input()
    string_2 = input()
    
    # Split input strings into lists
    string_list_1 = string_1.split()
    string_list_2 = string_2.split()
    
    # Initialize result counter
    result_counter = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert string elements to integers
        number_a = int(string_list_1[index])
        number_b = int(string_list_2[index])
        
        # Check if the elements are different
        if number_a != number_b:
            # Increment result if they are different
            result_counter += 1 
    
    # Determine and print the result based on the counter
    if result_counter < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
do_main()
