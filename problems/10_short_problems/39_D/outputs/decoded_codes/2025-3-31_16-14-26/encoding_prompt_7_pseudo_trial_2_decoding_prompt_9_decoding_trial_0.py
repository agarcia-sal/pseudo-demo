def main():
    # Read input from the user
    first_time_input = input()
    second_time_input = input()
    
    # Split the input strings into lists of strings
    first_time_parts = first_time_input.split()
    second_time_parts = second_time_input.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Compare the parts of both time inputs
    for index in range(3):  # We expect 3 parts (hours, minutes, seconds)
        first_part = int(first_time_parts[index])
        second_part = int(second_time_parts[index])
        
        # Increment the difference count if parts do not match
        if first_part != second_part:
            difference_count += 1 
    
    # Check if there are less than 3 differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    main()
