# Photo-Resizer

Here is a comprehensive overview and descriptive guide for the Python Image Resizer, Compressor, and PDF Converter script. You can use this description for a GitHub repository README, portfolio project documentation, or a blog post.

Python Image Processing & Conversion Utility
An all-in-one Python script built using the powerful Pillow (PIL) library designed to effortlessly handle everyday image manipulation tasks. Whether you need to downscale dimensions for web uploads, compress an image down to a strict file size limit in kilobytes (KB), or package images into a portable document format (PDF), this utility automates the workflow in a few lines of code.

Key Features
Pixel-Level Scaling: Resize images dynamically by exact pixel dimensions while intelligently preserving the original aspect ratio if only width or height is provided.

Target File Size Compression (KB): Iteratively compresses JPEGs by tuning quality settings to hit a specified target file size in kilobytes (ideal for portal uploads with strict file size caps).

Format Flexibility & Transparency Handling: Automatically converts images with alpha channels (PNG transparency or palette modes) into standard RGB to prevent saving errors when exporting to JPEG or PDF.

Instant PDF Conversion: Converts any standard image format (.jpg, .jpeg, .png) directly into a clean, standalone PDF document.

How It Works
Image Loading & Mode Correction: The script opens the target image using Pillow and checks its color mode (RGBA or P). If transparency or special palettes are detected, it converts the image to standard RGB.

Smart Resizing Logic:

By Pixel: Uses high-quality LANCZOS resampling to ensure minimal loss of image clarity.

By KB Size: Dynamically loops through compression quality reductions until the resulting file size aligns close to the requested target ceiling.

Export & Save: Outputs the processed asset cleanly to your specified file path with optimization flags enabled.
