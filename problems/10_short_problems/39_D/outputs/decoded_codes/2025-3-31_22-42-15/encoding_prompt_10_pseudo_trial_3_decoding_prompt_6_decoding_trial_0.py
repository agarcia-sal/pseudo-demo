def do_main():
    # Read two lines of input
    input_line_1 = input()
    input_line_2 = input()
    
    # Split the input strings into lists of strings
    list_of_strings_1 = input_line_1.split()
    list_of_strings_2 = input_line_2.split()
    
    # Initialize result count
    result_count = 0
    
    # Compare elements from both lists
    for index in range(3):
        # Convert string elements to integers
        first_value = int(list_of_strings_1[index])
        second_value = int(list_of_strings_2[index])
        
        # Check if the values are not equal
        if first_value != second_value:
            result_count += 1
    
    # Determine the result based on the comparison count
    if result_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
do_main()
