def main():
    # Read input values for both times
    first_time = input()
    second_time = input()
    
    # Split the input strings into lists of time components
    components1 = first_time.split()
    components2 = second_time.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Compare corresponding components of both times
    for index in range(3):  # We assume there are exactly 3 components for time
        # Convert components to integers
        value1 = int(components1[index])
        value2 = int(components2[index])
        
        # Check if the values are different
        if value1 != value2:
            difference_count += 1
            
    # Determine result based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the main function when the script runs
if __name__ == "__main__":
    main()
