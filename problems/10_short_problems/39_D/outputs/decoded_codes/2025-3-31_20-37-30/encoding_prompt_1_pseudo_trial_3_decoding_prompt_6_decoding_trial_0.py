def main():
    # Read input values for two sets of triplets
    first_triplet = input()
    second_triplet = input()
    
    # Split the input strings into individual components
    first_triplet_list = first_triplet.split()
    second_triplet_list = second_triplet.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Compare corresponding elements of the two triplets
    for index in range(3):  # Looping from 0 to 2
        # Convert the string elements to integers for comparison
        first_value = int(first_triplet_list[index])
        second_value = int(second_triplet_list[index])
        
        # Check if the values are different
        if first_value != second_value:
            # Increment the difference counter
            difference_count += 1

    # Determine if the number of differences is less than 3
    if difference_count < 3:
        print("YES")  # Indicating that the triplet is similar
    else:
        print("NO")   # Indicating that the triplet is not similar

# If the script is executed as the main program, call the main function
if __name__ == "__main__":
    main()
