import os
import re

def update_image_paths(directory):
    # Support all standard image extensions we replaced
    extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
    
    # Create regex pattern to match these extensions (case-insensitive)
    # (?![a-zA-Z]) ensures we don't accidentally match .jpg.tmp or something longer
    pattern = re.compile(r'\.(' + '|'.join(e.strip('.') for e in extensions) + r')(?![a-zA-Z])', re.IGNORECASE)

    target_file_extensions = {'.html', '.css', '.js'}

    files_modified = 0
    total_replacements = 0

    for root, _, files in os.walk(directory):
        # Skip some potential system or backup folders
        if '.git' in root or 'Traceback' in root or '__pycache__' in root:
            continue
            
        for file in files:
            if any(file.endswith(ext) for ext in target_file_extensions):
                filepath = os.path.join(root, file)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Replace extensions with .webp
                    new_content, num_subs = pattern.subn('.webp', content)
                    
                    if num_subs > 0:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated {filepath} ({num_subs} replacements)")
                        files_modified += 1
                        total_replacements += num_subs
                        
                except Exception as e:
                    print(f"Failed to process {filepath}: {e}")

    print(f"\nPath Update Complete! Modified {total_replacements} paths across {files_modified} files.")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    update_image_paths(current_dir)
