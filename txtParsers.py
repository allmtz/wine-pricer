import re


def saveAsTxtFile(content: str, title: str):
    formatedTitle = title.replace(' ', '-')
    file_path = f'./menus/parsed/{formatedTitle}.txt'

    with open(file_path, 'w') as file:
        file.write(content)
        print(f'{title} file saved')


def removeQuotationMarks(s):
    quotatioMarksRegx = r'[\'"]'
    return re.sub(quotatioMarksRegx, "", s)


# Could be more efficient by using a better regex to filter out the useless characters between the wine info and the price.
# Could also look into improving OCR results as that would make it much easier to parse the generated text.
def bhParser():
    path = './menus/text/Bounty-Hunter.txt'

    with open(path, 'r') as file:
        txt = file.read()
        lines = txt.split('\n')

        linesWithPrice = ''
        finalString = ''

        # Best regex so far, need to exclude periods
        # pattern = r'^.*?\.{2}.*\$(.*)'

        # Match anything that ends with a dollar sign follwed by any amount of characters ex: $1,123 or $12
        hasAPrice = r'.*\$(.*)$'
        for line in lines:
            match = re.search(hasAPrice, line)
            if match:
                linesWithPrice += match.group() + "\n"

        lines2 = linesWithPrice.split('\n')

        # Splicing out the characters between wine info and the price.
        # Not thorough, some funky characters make it through like ".j"
        for line in lines2:
            twoDotsIdx = line.find("..")
            dollarIdx = line.find("$")
            finalString += f'{line[0:twoDotsIdx]}  {line[dollarIdx:]}\n'

    return removeQuotationMarks(finalString.strip())


def RDparser():
    try:
        txt = open('./menus/text/RD.txt').read()
    except:
        print('Make sure the file being opened exists')

    finalString = ''

    wineStart = txt.find("SPARKLING")
    wineEnd = txt.find('COLD BEER')

    # Cut out the unrelated info
    wineSection = txt[wineStart:wineEnd].split('\n')

    # Regex to match prices and prices in the format "glass/bottle"
    hasPrice = r'\d+\/\d+|\d+'

    for line in wineSection:
        match = re.search(hasPrice, line)

        if match:
            # Add a dollar before the price
            s = line[:line.find(match.group())] + "$" + match.group() + '\n'
            finalString += s

    return removeQuotationMarks(finalString.strip())


# saveAsTxtFile(bhParser(), "Bounty-Hunter")
# saveAsTxtFile(RDparser(), 'RD')
