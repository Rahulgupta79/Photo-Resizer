import os
from PIL import Image

def resize_image(input_path, output_path, target_width=None, target_height=None, quality=85):
    """Resizes an image by pixel dimensions while maintaining aspect ratio."""
    with Image.open(input_path) as img:
        # Convert to RGB if saving as JPEG/PDF (removes alpha channel issues)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
            
        orig_width, orig_height = img.size
        
        if target_width and target_height:
            img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
        elif target_width:
            aspect_ratio = orig_height / orig_width
            new_height = int(target_width * aspect_ratio)
            img = img.resize((target_width, new_height), Image.Resampling.LANCZOS)
        elif target_height:
            aspect_ratio = orig_width / orig_height
            new_width = int(target_height * aspect_ratio)
            img = img.resize((new_width, target_height), Image.Resampling.LANCZOS)
            
        img.save(output_path, quality=quality, optimize=True)
    print(f"Image successfully resized by pixels and saved to: {output_path}")

def resize_image_by_kb(input_path, output_path, target_kb, tolerance=2):
    """Compresses/resizes a JPEG image iteratively to reach a target size in KB."""
    with Image.open(input_path) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
            
        quality = 95
        img.save(output_path, "JPEG", quality=quality)
        
        # Iteratively reduce quality to hit target file size
        while quality > 10:
            file_size_kb = os.path.getsize(output_path) / 1024
            if abs(file_size_kb - target_kb) <= tolerance or file_size_kb <= target_kb:
                break
            quality -= 5
            img.save(output_path, "JPEG", quality=quality, optimize=True)
            
    print(f"Image compressed to ~{os.path.getsize(output_path) / 1024:.2f} KB and saved to: {output_path}")

def convert_image_to_pdf(input_path, output_pdf_path):
    """Converts any JPG/JPEG/PNG image into a PDF file."""
    with Image.open(input_path) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(output_pdf_path, "PDF", resolution=100.0)
    print(f"Image successfully converted and saved as PDF: {output_pdf_path}")

# --- Example Usage ---
if __name__ == "__main__":
    # 1. Provide your source image path here
    source_image = "sample.jpg" 
    
    if os.path.exists(source_image):
        # Example A: Resize by pixels (e.g., width 800px)
        resize_image(source_image, "resized_output.jpg", target_width=800)
        
        # Example B: Resize/Compress to a target file size in KB (e.g., under 150 KB)
        resize_image_by_kb(source_image, "compressed_output.jpg", target_kb=150)
        
        # Example C: Convert image to PDF format
        convert_image_to_pdf(source_image, "converted_output.pdf")
    else:
        print(f"Please place an image named '{source_image}' in the script directory to run the examples.")
