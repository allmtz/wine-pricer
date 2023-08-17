import PyPDF2
import re


def mustardsParser():
    reader = PyPDF2.PdfReader("./menus/non-OCR/mustards.pdf")
    text = ''
    final = ''

    for page in reader.pages:
        text += page.extract_text() + "\n"

    # Remove '.' and whitespace from the text
    lines = text.replace('.', ' ').strip().split("\n")

    for line in lines:
        lastChar = line[-1]
        try:
            # If the last character is a number string, add a dollar sign and a new line
            int(lastChar)

            # Place the dollar sign 4 characters before the last number string
            # ex: '1000' -> '$1000'
            hasDollarSign = line[:-5] + '$' + line[-5:] + "\n"

            # Remove any whitespace between the dollar sign and the price
            final += re.sub(r'\$\s*', '$', hasDollarSign)

        except:
            # Not a number, don't add a newline
            final += line

    # Save the generated text
    with open('./menus/parsed/Mustards.txt', 'w') as file:
        file.write(final)
        print('Mustards file saved')


mustardsParser()
