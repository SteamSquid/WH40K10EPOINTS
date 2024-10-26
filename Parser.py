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
    # 1st [] is page 
    # 2nd [] is page element
    # 3rd [] 


    print(root[1][0][1].tag)
        


if __name__ == "__main__":
    main()