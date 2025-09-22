def do_main():
    # Get user input for two strings
    input_string_1 = input()
    input_string_2 = input()
    
    # Split input strings into lists
    list_1 = input_string_1.split()
    list_2 = input_string_2.split()
    
    # Initialize result counter
    difference_count = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert string elements to integers
        value_1 = int(list_1[index])
        value_2 = int(list_2[index])
        
        # Check if the elements are different
        if value_1 != value_2:
            # Increment result if they are different
            difference_count += 1 
    
    # Determine and print the result based on the counter
    if difference_count < 3:
        print("YES")
    else:
        print("NO")
        
# Main execution starts here
if __name__ == "__main__":
    do_main()
