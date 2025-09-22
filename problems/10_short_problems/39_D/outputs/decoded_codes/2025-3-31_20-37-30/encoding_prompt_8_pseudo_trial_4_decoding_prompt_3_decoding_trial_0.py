def main():
    # Prompt the user for two sets of numbers
    first_input = input()
    second_input = input()
    
    # Split the inputs into lists
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Compare corresponding elements from both lists
    for index in range(3):  # We expect exactly three elements in both lists
        # Convert the current elements to integers for comparison
        number_from_first_list = int(first_list[index])
        number_from_second_list = int(second_list[index])
        
        # Check if the numbers are different
        if number_from_first_list != number_from_second_list:
            difference_count += 1
            
    # Evaluate the number of differences 
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# This part indicates that the main function will run when the script is executed
if __name__ == "__main__":
    main()
