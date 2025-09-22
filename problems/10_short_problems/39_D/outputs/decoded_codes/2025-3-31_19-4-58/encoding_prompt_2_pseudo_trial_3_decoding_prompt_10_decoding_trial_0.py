def do_main():
    # Prompt the user for the first sequence of numbers
    first_input = input()
    # Prompt the user for the second sequence of numbers
    second_input = input()
    
    # Split the input sequences into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()

    # Initialize the difference counter
    difference_count = 0

    # Compare corresponding numbers in the two lists (up to the 3rd pair)
    for i in range(min(3, len(first_list), len(second_list))):
        first_number = int(first_list[i])
        second_number = int(second_list[i])
        
        if first_number != second_number:
            difference_count += 1

    # Check the count of differences and output the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main program execution
do_main()
