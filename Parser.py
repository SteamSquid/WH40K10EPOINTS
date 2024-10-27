import pandas as pd
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
    info = []

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


    
    
    page = root[1][0]

    
    for unit_box in page:
        unit=[]
        for text in unit_box:
            unit.append(text.text)
        info.append(unit)

    info = [unit for unit in info if unit != []]

    infoTemp = []

    for unitbox in info:
        unitbox = [element for element in unitbox if unitbox is not None]
        infoTemp.append(unitbox)


    for unitbox in info:
        unitbox = [element for element in unitbox if unitbox != []]
        infoTemp.append(unitbox)
    
    for element in infoTemp:
        print(element)


if __name__ == "__main__":
    main()