import os

# Replacements requested by user:
# 1. No grey text. Convert #555, #666, grey, gray to #000
# 2. linear-gradient(135deg, #FFD700, #DAA520) to linear-gradient(135deg, #00008B, #0000FF, #800080, #FFD700)

target_files = {'.html', '.css'}
replacements = {
    "#555": "#000",
    "#666": "#000",
    "color: grey": "color: #000",
    "color: gray": "color: #000",
    "linear-gradient(135deg, #FFD700, #DAA520)": "linear-gradient(135deg, #00008B, #0000FF, #800080, #FFD700)"
}

count_files = 0

# Start scanning
for root, _, files in os.walk('.'):
    if '.git' in root or 'Traceback' in root:
        continue
    for file in files:
        if any(file.endswith(ext) for ext in target_files):
            filepath = os.path.join(root, file)
            
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                new_content = content
                for old_val, new_val in replacements.items():
                    new_content = new_content.replace(old_val, new_val)
                    # Handle cases where they might be caps
                    new_content = new_content.replace(old_val.upper(), new_val)
                
                if new_content != content:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated colors in: {filepath}")
                    count_files += 1
            except Exception as e:
                print(f"Failed to read/write {filepath}: {e}")

print(f"\nColor Update Complete! Modified styles across {count_files} files.")
