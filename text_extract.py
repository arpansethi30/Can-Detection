from PIL import Image
import pytesseract
import re

# Load the image from file
image_path = "IMG_5848.jpg"
img = Image.open(image_path)

# Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(img)


# Define a function to search for nutritional info
def find_nutrition_info(label, text):
    pattern = rf"{label}\s*:\s*(\d+)"
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1)
    else:
        return "Not found"


# Extract nutritional information
calories = find_nutrition_info("Calories", text)
energy = find_nutrition_info("Energy", text)
carbs = find_nutrition_info("Carbs", text)

print(f"Calories: {calories}")
print(f"Energy: {energy}")
print(f"Carbs: {carbs}")
