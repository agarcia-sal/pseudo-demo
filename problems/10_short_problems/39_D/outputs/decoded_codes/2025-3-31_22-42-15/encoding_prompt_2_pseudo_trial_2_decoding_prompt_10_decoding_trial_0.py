def main():
    # Prompt the user for input
    first_input = input()
    second_input = input()
    
    # Split the input into separate components
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a variable to count differences
    difference_count = 0

    # Compare the components from both input lists
    for i in range(3):  # Assuming both lists have at least 3 elements
        first_value = int(first_list[i])
        second_value = int(second_list[i])
        
        if first_value != second_value:
            difference_count += 1

    # Determine the output based on differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to start the program
if __name__ == "__main__":
    main()


    1 2 3
    1 2 3
    

    1 2 3
    4 5 6
    

    1 2 3
    1 3 2
    