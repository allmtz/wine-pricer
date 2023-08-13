import pdf2image
import pytesseract

# Uncomment if tesseract isn't in $PATH
# pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# Relative path to each PDF
paths = {
    'Bounty Hunter': './menus/OCR/bounty-hunter.pdf',
    'RD': './menus/OCR/R&D.pdf',
    # Need to play around with OCR to process these more accurately
    # 'Brix': './menus/OCR/brix.pdf',
    # 'Charter Oak': './menus/OCR/charter-oak.pdf',
}


# Return a list of images
def getImagesFromPDFpath(path: str):
    return pdf2image.convert_from_path(path)


# Use tesseract to perform OCR on a list of images
def imagesToText(images: list):
    text = ''
    for image in images:
        text += pytesseract.image_to_string(image)
    return text


def saveAsTxtFile(content: str, title: str):
    formatedTitle = title.replace(' ', '-')
    file_path = f'./menus/text/{formatedTitle}.txt'
    # Open the file for writing
    with open(file_path, 'w') as file:
        # Write the string to the file
        file.write(content)


# Main loop
for restaurant, path in paths.items():
    images = getImagesFromPDFpath(path)
    text = imagesToText(images)
    saveAsTxtFile(text, restaurant)
