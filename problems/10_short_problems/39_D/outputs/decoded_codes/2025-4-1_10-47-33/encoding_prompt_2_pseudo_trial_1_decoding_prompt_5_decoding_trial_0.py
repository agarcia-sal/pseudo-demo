def main():
    # Receive input from the user
    first_list = input()
    second_list = input()
    
    # Split the input strings into lists of values
    first_elements = first_list.split()
    second_elements = second_list.split()
    
    # Initialize a counter for the differences
    difference_count = 0
    
    # Compare corresponding elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        current_first_value = int(first_elements[index])
        current_second_value = int(second_elements[index])
        
        # If the values are different, increment the count
        if current_first_value != current_second_value:
            difference_count += 1
    
    # Check the number of differences and output the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Invoke the main function to begin execution
main()
