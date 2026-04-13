import os
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow library is not installed. Please run: pip install Pillow")
    exit(1)

def convert_images_to_webp(folder_path, quality=75):
    # Supported image extensions
    extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff'}
    
    path = Path(folder_path)
    if not path.exists():
        print(f"Directory {folder_path} does not exist.")
        return

    count = 0
    for file_path in path.rglob('*'):
        # Check if it's a supported format based on extension
        if file_path.is_file() and file_path.suffix.lower() in extensions:
            # Create new file path with .webp extension
            webp_path = file_path.with_suffix('.webp')
            
            # Skip if webp already exists so we don't duplicate work
            if webp_path.exists():
                print(f"Skipping {file_path.name} (WebP already exists)")
                continue
                
            try:
                # Open and convert image
                with Image.open(file_path) as img:
                    # WebP supports transparency, so we don't need to drop alpha channels 
                    # from PNGs, Pillow handles it correctly.
                    img.save(webp_path, 'WEBP', quality=quality)
                print(f"Converted: {file_path.name} -> {webp_path.name}")
                count += 1
            except Exception as e:
                print(f"Error converting {file_path.name}: {e}")
                
    print(f"\nOptimization complete! Successfully converted {count} images to WebP.")

if __name__ == "__main__":
    # We target the "Images" folder relative to this script
    images_dir = os.path.join(os.path.dirname(__file__), 'Images')
    print(f"Scanning for images in: {images_dir}")
    convert_images_to_webp(images_dir, quality=75)
