def do_main():
    # Read two strings representing scores
    first_score_string = input()
    second_score_string = input()
    
    # Split the input strings into lists of scores
    first_scores = first_score_string.split()
    second_scores = second_score_string.split()
    
    # Initialize a counter for score differences
    score_difference_count = 0 
    
    # Iterate over the first three scores
    for index in range(3):
        # Convert string scores to integers
        first_score = int(first_scores[index])
        second_score = int(second_scores[index])
        
        # Check if the scores are different
        if first_score != second_score:
            # Increment the difference counter
            score_difference_count += 1 

    # Determine if the number of differences is less than 3
    if score_difference_count < 3:
        print("YES")
    else:
        print("NO")
    
# Execute the main function
do_main()
