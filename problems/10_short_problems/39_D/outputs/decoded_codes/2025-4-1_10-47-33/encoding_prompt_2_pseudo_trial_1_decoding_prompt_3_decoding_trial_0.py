def main():
    # Step 1: Receive Input
    first_list = input()
    second_list = input()
    
    # Step 2: Split Input into Lists
    first_elements = first_list.split()
    second_elements = second_list.split()
    
    # Step 3: Initialize a Counter
    difference_count = 0
    
    # Step 4: Compare Corresponding Elements
    for index in range(3):
        # Convert the current values to integers
        current_first_value = int(first_elements[index])
        current_second_value = int(second_elements[index])
        
        # Check if the current values are different
        if current_first_value != current_second_value:
            difference_count += 1
            
    # Step 5: Check Number of Differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 6: Invoke Main Function to Begin Execution
main()
