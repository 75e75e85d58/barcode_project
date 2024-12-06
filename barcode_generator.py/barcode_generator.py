import barcode
from barcode.writer import ImageWriter

def generate_barcode():
    # Step 1: Display supported barcode formats
    print("Supported barcode formats:")
    supported_barcodes = barcode.PROVIDED_BARCODES
    for i, b in enumerate(supported_barcodes, 1):
        print(f"{i}. {b}")

    # Step 2: Let the user select the barcode format
    while True:
        try:
            user_choice = int(input("\nEnter the number corresponding to the barcode format you want to use: "))
            if 1 <= user_choice <= len(supported_barcodes):
                selected_format = list(supported_barcodes)[user_choice - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(supported_barcodes)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"\nYou selected: {selected_format}")

    # Step 3: User inputs the text for the barcode
    while True:
        text = input("Enter the text for the barcode (alphanumeric characters only): ")
        if text.strip():
            break
        print("The text cannot be empty. Please enter valid text.")

    # Step 4: Generate the barcode
    try:
        code = barcode.get_barcode_class(selected_format)
        image = code(text, writer=ImageWriter())
        
        # Step 5: Save the barcode image
        file_name = input("Enter the file name to save the barcode image (without extension): ").strip()
        if not file_name:
            file_name = "barcode"
        image.save(file_name)
        
        print(f"\nBarcode saved successfully as '{file_name}.png'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the barcode generator
if __name__ == "__main__":
    generate_barcode()
