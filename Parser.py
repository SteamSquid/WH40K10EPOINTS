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

    # the array that is used to pretty up the pages
    infoTemp = []

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
    page = root[1][0]

    
    for unit_box in page:
        unit=[]
        for text in unit_box:
            unit.append(text.text)
        info.append(unit)

    # Pretty up the page
    info = [unit for unit in info if unit != []]

    
    # Pretty up the units
    for unitbox in info:
        unitbox = [element for element in unitbox if element is not None]
        infoTemp.append(unitbox)

    # Pretty the unity even more
    for unitbox in info:
        unitbox = [element for element in unitbox if element != []]
        infoTemp.append(unitbox)

    info = infoTemp
    
    #clear infoTemp
    infoTemp = []
    
    """
    for thing in info:
        print(thing)
    """

    # Correctly seprate the units
    for unitbox in info:
        tempBox = []
        for element in unitbox:

            tempElement = []

            if element is not None and '.' in element:
                tempElement = element.split('.')
                tempElement=[thing for thing in tempElement if thing != '']
            else:
                tempBox.append(element)
             
            for ting in tempElement:
                tempBox.append(ting)
            


        infoTemp.append(tempBox)
    
    info = infoTemp
    
    
    for thing in info:
        print(thing)

if __name__ == "__main__":
    main()