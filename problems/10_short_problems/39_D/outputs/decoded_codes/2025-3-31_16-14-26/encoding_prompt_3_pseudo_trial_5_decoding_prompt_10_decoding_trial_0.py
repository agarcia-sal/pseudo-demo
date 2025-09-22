def do_main():
    # Get input from the user
    input_string1 = input()
    input_string2 = input()
    
    # Split each input string into a list of words
    list1 = input_string1.split()
    list2 = input_string2.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Compare each corresponding element in the two lists
    for index in range(3):
        try:
            # Convert the current elements to integers
            value_from_list1 = int(list1[index])
            value_from_list2 = int(list2[index])
            
            # Check if the values are different
            if value_from_list1 != value_from_list2:
                # Increment the difference count
                difference_count += 1
        except (ValueError, IndexError):
            # Handle cases where conversion fails or the list is shorter
            difference_count += 1
            
    # Evaluate the total number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main block to execute the function
if __name__ == "__main__":
    do_main()
