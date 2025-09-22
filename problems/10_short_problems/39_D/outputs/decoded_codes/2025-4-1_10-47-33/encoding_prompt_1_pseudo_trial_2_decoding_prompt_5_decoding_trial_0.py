def main():
    # Read input values from the user
    user_input1 = input()
    user_input2 = input()
    
    # Split the input strings into lists
    list1 = user_input1.split()
    list2 = user_input2.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert current elements to integers
        value_from_list1 = int(list1[index])
        value_from_list2 = int(list2[index])
        
        # Check if the values are different
        if value_from_list1 != value_from_list2:
            # Increment the difference counter
            difference_count += 1 
    
    # Evaluate the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
