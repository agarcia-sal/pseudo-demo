input_string = input()[:-1]  # Read input and strip the last character
length_of_string = len(input_string)
longest_repeated_length = 0

for substring_length in range(length_of_string):
    for index in range(length_of_string):
        current_substring = input_string[index:index + substring_length]
        
        if input_string.find(current_substring, index + 1) != -1:
            longest_repeated_length = substring_length
            break  # Exit inner loop as we found a repeated substring of this length
    else:
        continue  # Only executed if inner loop did NOT break
    break  # Exit outer loop once we found a repeated substring

print(longest_repeated_length)
