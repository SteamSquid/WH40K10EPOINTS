import pdfquery
import xml.etree.ElementTree as ET
import io


def main():
    """
    This is a parser I am writing to help Zyphyr.
    They want to parse the warhammer 40k army points.
    It can't be that hard right?
    """
    # THe ne of the MUNITORUM FIELD MANUAL
    PDF_Name="MunitionsManul.pdf"

    # The name of the XML file to be parsed
    XML_Name="munitionsManual.xml"

    # The array that all the units will be stored in
    pageInfo= []

    # the array that is used to pretty up the pages
    infoTemp = []

    book = []
    """
    # Opening the PDF and convert it to an XML
    pdf = pdfquery.PDFQuery(PDF_Name)
    pdf.load()
    pdf.tree.write(XML_Name, pretty_print = True)
    """

    # Parsing the XML and getting its root
    tree = ET.parse(XML_Name)
    root = tree.getroot()

    # Print the things
    # root is base of tree
    # 1st [] is page                        tag: LTPage
    # 2nd [] is large elements on page      tag: LTRect, LTImage, LTFigure
    # 3rd [] is something I don't know yet  tag: LTTextLineHorizontal 
    # 4th [] the jucy bity we want          tag: LTTextBoxHorizontal 


    
    # Grab everything from the page
    #page = root[1][0]
    i = 0

    for page in root[1:]:
        page = page[0]
        pageInfo = []

        for unitBox in page:
            unit=[]
            for text in unitBox:
                unit.append(text.text)
            pageInfo.append(unit)

        # Remove the emty arrays from the page
        pageInfo = [unit for unit in pageInfo if unit != []]


        # Remove the empty arrays from the unit box 
        for unitBox in pageInfo:
            unitBox = [element for element in unitBox if element != []]
            infoTemp.append(unitBox)

        pageInfo = infoTemp

        #clear infoTemp
        infoTemp = []

        # Correctly seprate the units
        for unitBox in pageInfo:
            tempBox = []
            for unit in unitBox:
                tempUnit = []

                if unit is not None and '.' in unit:
                    tempUnit = unit.split('.')
                    tempUnit=[part for part in tempUnit if part != '']
                else:
                    tempBox.append(unit)

                for part in tempUnit:
                    tempBox.append(part)

            infoTemp.append(tempBox)

        pageInfo = infoTemp
        infoTemp = []
        book.append(pageInfo)

    for page in book:
        print(page)
        print("\n\n")
    
    

if __name__ == "__main__":
    main()