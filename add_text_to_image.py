import os
import sys
from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image_path, output_path, text):
    image = Image.open(image_path)
    
    # Convert RGBA to RGB to handle transparency issues
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    
    draw = ImageDraw.Draw(image)

    # Use a smaller font size (half the previous size)
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 12)

    width, height = image.size

    # Get text size using textbbox
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    # Calculate text position
    x = width - text_width - 10  # Adjusted margin for smaller text
    y = height - text_height - 10  # Adjusted margin for smaller text

    # Draw a smaller black rectangle as the background for the text
    draw.rectangle([x - 5, y - 5, x + text_width + 5, y + text_height + 5], fill="black")

    # Add the smaller white text on top of the black rectangle
    draw.text((x, y), text, font=font, fill="white")

    # Save the image
    image.save(output_path)

def process_directory(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('png', 'jpg', 'jpeg')):
            image_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)
            add_text_to_image(image_path, output_path, filename)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python add_text_to_images.py <input_directory> <output_directory>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]

    process_directory(input_directory, output_directory)
