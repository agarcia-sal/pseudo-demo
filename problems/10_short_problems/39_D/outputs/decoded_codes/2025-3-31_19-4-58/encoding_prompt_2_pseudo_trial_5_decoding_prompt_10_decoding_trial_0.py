def do_main():
    # Prompt the user to enter the first string of numbers
    first_input = input()
    
    # Prompt the user to enter the second string of numbers
    second_input = input()
    
    # Split the input strings into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Loop through the indices 0 to 2
    for index in range(3):
        # Convert strings to integers
        first_number = int(first_list[index])
        second_number = int(second_list[index])
        
        # Check if the two numbers are different
        if first_number != second_number:
            difference_count += 1

    # Output result based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Invoke the function to execute the program
do_main()
