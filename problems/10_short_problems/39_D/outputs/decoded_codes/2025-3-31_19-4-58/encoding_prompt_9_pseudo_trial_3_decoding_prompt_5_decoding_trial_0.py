# Start Main Program
def main():
    # Prompt the user for the first set of integers
    first_set = input()
    # Prompt the user for the second set of integers
    second_set = input()
    
    # Split input strings into lists
    first_list = first_set.split()
    second_list = second_set.split()
    
    # Initialize difference counter
    difference_count = 0
    
    # Check each position for differences
    for index in range(3):  # We expect exactly three integers
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer
        
        # If values differ, increment the count
        if first_value != second_value:
            difference_count += 1
            
    # Evaluate number of differences
    if difference_count < 3:
        print("YES")  # Displays "YES" if differences are less than 3
    else:
        print("NO")  # Displays "NO" if differences are 3 or more

# End Program
main()
