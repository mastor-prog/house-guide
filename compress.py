import os
from PIL import Image

def compress_images(directory, max_dimension=1200, quality=75):
    supported_formats = {'.jpg', '.jpeg', '.png'}
    for filename in os.listdir(directory):
        ext = os.path.splitext(filename)[1].lower()
        if ext in supported_formats:
            filepath = os.path.join(directory, filename)
            try:
                img = Image.open(filepath)
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                width, height = img.size
                if width > max_dimension or height > max_dimension:
                    if width > height:
                        new_width = max_dimension
                        new_height = int((max_dimension / width) * height)
                    else:
                        new_height = max_dimension
                        new_width = int((max_dimension / height) * width)
                    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                img.save(filepath, 'JPEG', optimize=True, quality=quality)
                print(f'Compressed: {filename}')
            except Exception as e:
                print(f'Failed to compress {filename}: {e}')

compress_images(r'd:\Antivigravity\House_guide_v01\assets\images')
