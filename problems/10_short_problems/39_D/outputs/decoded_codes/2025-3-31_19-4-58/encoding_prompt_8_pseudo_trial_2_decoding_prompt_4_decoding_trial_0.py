def main():
    # Read two sets of input from the user
    first_set = input()
    second_set = input()
    
    # Split the input strings into individual elements
    first_values = first_set.split()
    second_values = second_set.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through each pair of corresponding values
    for index in range(3):  # since we know there are exactly 3 values
        # Convert the string values to integers
        value_from_first_set = int(first_values[index])
        value_from_second_set = int(second_values[index])
        
        # Check if the values are different
        if value_from_first_set != value_from_second_set:
            difference_count += 1 
    
    # Check if the number of differences is less than three
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution begins here
main()
