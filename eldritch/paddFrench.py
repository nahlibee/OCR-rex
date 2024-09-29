import cv2
import os
import shutil
from paddleocr import PaddleOCR

# Paths
img_path = r'C:\Users\yahya\Desktop\ocrscan\ressources\inputs\cin4.jpg'
lines_output_folder = r'C:\Users\yahya\Desktop\ocrscan\outputs\lines'  # Folder to save the line images
characters_output_folder = r'C:\Users\yahya\Desktop\ocrscan\outputs\characters'  # Folder to save the character images

# Function to clean folders
def clean_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)

# Clean output folders
clean_folder(lines_output_folder)
clean_folder(characters_output_folder)

# Load image
img = cv2.imread(img_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Initialize PaddleOCR for Arabic and Latin (French)
ocr = PaddleOCR(lang='ar', use_angle_cls=True)  # 'ar' for Arabic

# Perform OCR
result = ocr.ocr(img_rgb)

# Print the result to understand its structure
print("OCR Result:", result)

# Extract text lines and their bounding boxes
words_info = []

for line in result:
    for word_info in line:
        if word_info:
            box = word_info[0]  # Bounding box
            text = word_info[1][0]  # Text
            score = word_info[1][1]  # Score
            words_info.append((box, text, score))

# Sort words by their y-coordinate (average of the top-left and bottom-left corners)
words_info.sort(key=lambda w: (w[0][0][1] + w[0][3][1]) / 2)

# Group words into lines based on vertical and horizontal proximity
lines = []
current_line = []
line_threshold = 40  # Vertical distance threshold to consider words in the same line

for i, (box, text, score) in enumerate(words_info):
    if not current_line:
        current_line.append((box, text, score))
    else:
        prev_box = current_line[-1][0]
        if abs((box[0][1] + box[3][1]) / 2 - (prev_box[0][1] + prev_box[3][1]) / 2) < line_threshold:
            current_line.append((box, text, score))
        else:
            lines.append(current_line)
            current_line = [(box, text, score)]
if current_line:
    lines.append(current_line)

# Combine words in each line into a single string
combined_boxes = []

for line in lines:
    # Combine bounding boxes by taking the min and max coordinates
    x_coords = [coord[0] for word in line for coord in word[0]]
    y_coords = [coord[1] for word in line for coord in word[0]]
    combined_box = [[min(x_coords), min(y_coords)], [max(x_coords), min(y_coords)], [max(x_coords), max(y_coords)], [min(x_coords), max(y_coords)]]
    combined_boxes.append(combined_box)

# Extract and save bounding boxes as individual images
line_images = []

for line_idx, box in enumerate(combined_boxes):
    # Extract the coordinates from the bounding box
    x_min = int(min(point[0] for point in box))
    y_min = int(min(point[1] for point in box))
    x_max = int(max(point[0] for point in box))
    y_max = int(max(point[1] for point in box))
    
    # Crop the image using the bounding box coordinates
    cropped_img = img[y_min:y_max, x_min:x_max]
    line_images.append(cropped_img)
    
    # Save the cropped image
    output_path = os.path.join(lines_output_folder, f'line_{line_idx}.png')
    cv2.imwrite(output_path, cropped_img)

print(f"Cropped line images saved to {lines_output_folder}")

# Initialize PaddleOCR for character detection (considering 'ar' for Arabic)
ocr_char = PaddleOCR(lang='ar', use_angle_cls=True)  # 'ar' for Arabic

# Process each line image for character detection and output the result as one sentence
for line_idx, line_img in enumerate(line_images):
    result_char = ocr_char.ocr(line_img)
    
    # Check if the result_char is not None
    if result_char is not None:
        full_sentence = ""
        for line in result_char:
            if line:
                for word_info in line:
                    if word_info:
                        text = word_info[1][0]  # Text
                        full_sentence += text + " "
        
        # Print the full sentence for this line image
        print(f"Line {line_idx}: {full_sentence.strip()}")
        
        # Save the full sentence to a text file
        with open(os.path.join(characters_output_folder, f'line_{line_idx}.txt'), 'w', encoding='utf-8') as f:
            f.write(full_sentence.strip())

print(f"Cropped character images and sentences saved to {characters_output_folder}")

