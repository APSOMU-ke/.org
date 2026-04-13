import os
import json

base_dir = r"c:\Users\victor\3D Objects\APSOMU"
images_dir = os.path.join(base_dir, "Images")
js_output = os.path.join(base_dir, "js", "gallery-data.js")

folders = ["Members", "Launching", "Public Lecture", "County Assembly", "AGM"]

gallery_data = {}

for folder in folders:
    folder_path = os.path.join(images_dir, folder)
    if not os.path.exists(folder_path):
        print(f"Warning: Folder {folder_path} does not exist.")
        gallery_data[folder] = []
        continue

    all_files = os.listdir(folder_path)
    
    base_names = {}
    
    for f in all_files:
        ext = os.path.splitext(f)[1].lower()
        if ext not in ['.webp', '.jpg', '.jpeg', '.png', '.gif']:
            continue
            
        base = os.path.splitext(f)[0]
        # Deduplicate, prioritizing .webp format
        if base not in base_names:
            base_names[base] = f
        else:
            if ext == '.webp':
                base_names[base] = f

    # Convert to standard forward-slash paths relative to project root
    valid_files = [f"Images/{folder}/{fname}" for fname in base_names.values()]
    gallery_data[folder] = valid_files

# Create js/ folder if missing
os.makedirs(os.path.dirname(js_output), exist_ok=True)

# Write as standard JS variable
with open(js_output, "w", encoding="utf-8") as f:
    f.write("/**\n * AUTO-GENERATED FILE. DO NOT EDIT MANUALLY.\n * Run `python generate_gallery.py` to rebuild.\n */\n")
    f.write(f"const galleryData = {json.dumps(gallery_data, indent=4)};\n")

print(f"Successfully generated JS gallery index with {sum(len(v) for v in gallery_data.values())} total unique images.")
