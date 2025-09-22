def do_main():
    # Get input from the user
    input_string1 = input()  # First input string
    input_string2 = input()  # Second input string
    
    # Split each input string into a list of strings
    list1 = input_string1.split()  # List of words from first input
    list2 = input_string2.split()  # List of words from second input
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Compare each corresponding element in the two lists
    for index in range(3):  # Assumption: there will be at least 3 elements in each list
        # Convert the current elements to integers
        value_from_list1 = int(list1[index])
        value_from_list2 = int(list2[index])
        
        # Check if the values are different
        if value_from_list1 != value_from_list2:
            # Increment the difference count
            difference_count += 1
            
    # Evaluate the total number of differences
    if difference_count < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")  # 3 or more differences

# Main block to execute the function
if __name__ == "__main__":
    do_main()
