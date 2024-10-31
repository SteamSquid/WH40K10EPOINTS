from py_pdf_parser.loaders import load_file
from py_pdf_parser.visualise import visualise


# The name of the MUNITORUM FIELD MANUAL
PDF_Name = "MunitionsManul.pdf"

# The regex search used to identify the group headers for different groups
REGEX_SEARCH = "CODEX:*|INDEX:*"

# Load the PDF into the parser
document = load_file(PDF_Name)

# Create an ElementList containing all the teams or whatever
codexlist = document.elements.filter_by_regex(REGEX_SEARCH)

# Tag all the headers as headers
codexlist.add_tag_to_elements("Group Header")

# Create an empty list for holding the sections in document
sectionlist = []

# Iterate over the headers to create sections
for item in codexlist:
    # Try to get the next item in the list
    try:
        nextitem = codexlist.move_forwards_from(item)
    # If we're at the end of the list, it throws an exception. On execpt, get everything after the current item and then make that the last section
    except:
        last_section = document.elements.after(item)
        sectionlist.append(
            document.sectioning.create_section(
                name=item.text(),
                start_element=item,
                end_element=last_section[-1]
                )
            )
    else:
        sectionlist.append(
            document.sectioning.create_section(
                name=item.text(),
                start_element=item,
                end_element=nextitem,
                include_last_element=False
                )
            )

# Display a visualization of the current parsed file after all changes/tags
visualise(document)

"""
def main():

    This is a parser I am writing to help Zyphyr.
    They want to parse the warhammer 40k army points.
    It can't be that hard right?

    # The name of the MUNITORUM FIELD MANUAL
    PDF_Name="MunitionsManul.pdf"

    # The name of the XML file to be parsed
    #XML_Name="munitionsManual.xml"

    # The array that all the units will be stored in
    info = []

    # Opening the PDF and convert it to an XML
    pdf = pdfquery.PDFQuery(PDF_Name)
    pdf.load()
    #pdf.tree.write(XML_Name, pretty_print = True)

    # Parsing the XML and getting its root
    tree = ET.parse(XML_Name)
    root = tree.getroot()

    # Print the things
    # root is base of tree
    # 1st [] is page                        tag: LTPage
    # 2nd [] is large elements on page      tag: LTRect, LTImage, LTFigure
    # 3rd [] is something I don't know yet  tag: LTTextLineHorizontal 
    # 4th [] the jucy bity we want          tag: LTTextBoxHorizontal 


    print(tree)
    print(root)
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
"""
