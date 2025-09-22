def main():
    # Read input strings from the user
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of words
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a counter for differences
    difference_counter = 0 
    
    # Iterate through the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the values from both lists are different
        if first_value != second_value:
            # Increment the difference counter
            difference_counter += 1 
    
    # After comparing all three values, check the difference counter
    if difference_counter < 3:
        print("YES")
    else:
        print("NO")

# Trigger the main function when the program starts
main()
