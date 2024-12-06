import barcode
from barcode.writer import ImageWriter

# Input text for the barcode
text = "Python_Programming_Code"  # Replace spaces with underscores or other symbols
text1 = str(text)

# Generate a barcode using the Code128 standard
code = barcode.get_barcode_class("code128")
image = code(text1, writer=ImageWriter())

# Save the barcode image
save_img = image.save("my_final_barcode")

print("Barcode saved successfully as 'my_final_barcode.png'")
