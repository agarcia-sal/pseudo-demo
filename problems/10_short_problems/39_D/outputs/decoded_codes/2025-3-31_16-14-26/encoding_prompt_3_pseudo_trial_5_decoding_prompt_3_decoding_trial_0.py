def do_main():
    # Get input from the user
    input_string1 = input()  # First input string
    input_string2 = input()  # Second input string
    
    # Split each input string into a list of strings
    list1 = input_string1.split()  # List from first input
    list2 = input_string2.split()  # List from second input
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Compare each corresponding element in the two lists
    for index in range(3):  # We only compare the first three elements
        value_from_list1 = int(list1[index])  # Convert to integer
        value_from_list2 = int(list2[index])  # Convert to integer
        
        # Check if the values are different
        if value_from_list1 != value_from_list2:
            # Increment the difference count
            difference_count += 1
            
    # Evaluate the total number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main block to execute the function
if __name__ == "__main__":
    do_main()
