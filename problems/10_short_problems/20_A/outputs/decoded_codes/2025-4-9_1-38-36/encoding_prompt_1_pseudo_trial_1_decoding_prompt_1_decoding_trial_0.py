# Step 1: Read the input
raw_input = input()  # Read input from standard input
cleaned_input = raw_input.strip()  # Clean the input by trimming white spaces

# Step 2: Normalize the file path (function needed)
def normalize_path(path):
    # Implement normalization logic here (to be defined)
    # For now, we'll return the path as is; in real code, it would normalize the path.
    return path

normalized_path = normalize_path(cleaned_input)  # Normalize the file path

# Step 3: Format the path to ensure it starts with one '/'
if normalized_path.startswith('//'):  # Check if it starts with two or more '/'
    formatted_path = '/' + normalized_path.lstrip('/')  # Replace with a single '/'
else:
    formatted_path = normalized_path  # Keep it as is

# Step 4: Output the final formatted path
print(formatted_path)  # Print the final formatted path
