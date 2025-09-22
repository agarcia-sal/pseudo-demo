def do_main():
    # Input two strings containing numbers
    input_string_1 = input()
    input_string_2 = input()
    
    # Split input strings into lists of strings
    number_list_1 = input_string_1.split()
    number_list_2 = input_string_2.split()
    
    # Initialize the result counter
    result_counter = 0
    
    # Loop to compare the first three elements
    for index in range(3):
        # Convert string elements to integers
        first_number = int(number_list_1[index])
        second_number = int(number_list_2[index])
        
        # Compare the two integers
        if first_number != second_number:
            result_counter += 1
    
    # Determine the result based on the count of differences
    if result_counter < 3:
        print("YES")
    else:
        print("NO")

# Entry point for program execution
if __name__ == "__main__":
    do_main()
