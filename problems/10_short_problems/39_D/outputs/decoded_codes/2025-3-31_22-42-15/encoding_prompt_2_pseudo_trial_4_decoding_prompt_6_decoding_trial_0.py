def main():
    # Prompt the user for input and store the first input
    first_input = input()
    
    # Prompt the user for another input and store it
    second_input = input()
    
    # Split the inputs into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a variable to track how many elements differ
    differences_count = 0
    
    # Loop three times to check corresponding elements
    for i in range(3):
        # Convert the corresponding elements into integers
        first_value = int(first_list[i])
        second_value = int(second_list[i])
        
        # Check if the values differ
        if first_value != second_value:
            differences_count += 1
    
    # Check if the number of differences is less than 3
    if differences_count < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()
