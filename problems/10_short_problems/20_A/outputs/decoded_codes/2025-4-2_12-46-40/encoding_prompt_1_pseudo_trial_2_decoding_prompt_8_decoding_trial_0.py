import os

def normalize_path(input_string):
    normalized_path = os.path.normpath(input_string)
    return normalized_path

def clean_path(normalized_path):
    cleaned_path = normalized_path.lstrip('/').rjust(len(normalized_path), '/')
    return cleaned_path

# Start Program
input_string = input().strip()  # Step 2: Get Input
normalized_path = normalize_path(input_string)  # Step 3: Normalize Path
cleaned_path = clean_path(normalized_path)  # Step 4: Clean Path
print(cleaned_path)  # Step 5: Output Result
# End Program
