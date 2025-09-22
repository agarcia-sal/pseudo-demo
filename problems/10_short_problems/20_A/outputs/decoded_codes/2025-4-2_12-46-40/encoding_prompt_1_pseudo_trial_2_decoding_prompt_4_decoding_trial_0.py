import os

def normalize_path(input_string):
    """
    Normalize the input file path, resolving relative path components.
    
    Parameters:
    input_string (str): The raw input string representing a file path.
    
    Returns:
    str: The normalized file path.
    """
    return os.path.normpath(input_string)

def clean_path(normalized_path):
    """
    Clean the normalized path by replacing leading forward slashes with a single slash.
    
    Parameters:
    normalized_path (str): The normalized file path.
    
    Returns:
    str: The cleaned file path.
    """
    return '/' + normalized_path.lstrip('/')

def main():
    # Step 2: Get Input
    input_string = input().strip()
    
    # Step 3: Normalize Path
    normalized_path = normalize_path(input_string)
    
    # Step 4: Clean Path
    cleaned_path = clean_path(normalized_path)
    
    # Step 5: Output Result
    print(cleaned_path)

# Step 1: Start Program
if __name__ == "__main__":
    main()
