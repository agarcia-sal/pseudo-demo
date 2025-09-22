def main():
    # Read input values for the two times
    first_time = input()
    second_time = input()
    
    # Split the input strings into lists of components
    components_1 = first_time.split()
    components_2 = second_time.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Compare corresponding components of both times
    for index in range(3):  # Assuming time format has 3 components (e.g. HH MM SS)
        # Convert components to integers
        value_1 = int(components_1[index])
        value_2 = int(components_2[index])
        
        # Check if the values are different
        if value_1 != value_2:
            difference_count += 1
            
    # Determine result based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the main function when the script runs
if __name__ == "__main__":
    main()
