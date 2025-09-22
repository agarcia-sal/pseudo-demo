import re  # Importing regular expression module for string manipulation

# Function to remove leading and trailing whitespace from the input string
def remove_whitespace(input_string):
    return input_string.strip()

# Function to normalize the path - for demonstration, this will assume it replaces backslashes with slashes
def normalize_path(input_string):
    return input_string.replace('\\', '/')

# Function to replace multiple leading slashes with a single slash
def replace_multiple_leading_slashes(input_string):
    return re.sub(r'^/+','/', input_string)  # Using regex to replace multiple leading slashes

# Main logic starts here
raw_input = input()  # Reading input
normalized_path = remove_whitespace(raw_input)  # Removing whitespace from input
normalized_path = normalize_path(normalized_path)  # Normalizing the path
modified_path = replace_multiple_leading_slashes(normalized_path)  # Replacing leading slashes

# Output the final modified path
print(modified_path)
