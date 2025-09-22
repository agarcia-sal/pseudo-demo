import re  # Importing 're' module for regular expressions

# Function to normalize the input path (assuming a simple placeholder normalization)
def normalize(input_path):
    # Simply returning the input path for demonstration (real implementation would handle specific rules)
    return input_path

# Function to replace leading slashes with a single slash
def replace_leading_slashes(input_path):
    # Using regular expression to replace multiple leading slashes with a single one
    return re.sub(r'^/{2,}', '/', input_path)

# Start of the program
input_string = input()  # Read input from the user

normalized_path = normalize(input_string)  # Normalize the input path
cleaned_path = replace_leading_slashes(normalized_path)  # Clean the path

print(cleaned_path)  # Print the cleaned path to the output
