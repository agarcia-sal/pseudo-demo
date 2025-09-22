def main():
    # Read two lines of input representing two sets of data
    input_set1 = input()
    input_set2 = input()
    
    # Split the input strings into lists of values
    values_set1 = input_set1.split()
    values_set2 = input_set2.split()

    # Initialize a counter for differences
    difference_count = 0
    
    # Compare corresponding items in both sets
    for index in range(3):  # Assuming we're only comparing the first three values
        # Convert the current items to integers for comparison
        current_value1 = int(values_set1[index])
        current_value2 = int(values_set2[index])
        
        # Check if the current values are different
        if current_value1 != current_value2:
            # Increment the counter if values are different
            difference_count += 1
    
    # Determine if there are fewer than 3 differences
    if difference_count < 3:
        print("YES")  # Output indicating similarities
    else:
        print("NO")  # Output indicating significant differences

# Main execution starts here
if __name__ == "__main__":
    main()
