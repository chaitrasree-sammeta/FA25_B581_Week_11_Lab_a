from lxml import etree  # Importing the lxml library's etree module for XML handling
from pathlib import Path  # Importing Path from pathlib to manage file paths

# Define the directory where the XML file will be saved
data_dir = Path.cwd() / 'data'

# Define the file path for the output XML file
sample_xml_output_file = data_dir / 'exercise_1.xml'

# Create the root element of the XML tree, <note>
root = etree.Element("note")

# Create a child element <to> with an attribute 'priority' and set the text content
to = etree.SubElement(root, "to", attrib={"priority": "moderate", "type": "Meet up for lunch"})
# Set the text content of the <to> element to "George"
to.text = "Shannu"

# Create a child element <from> and set its text content
from_ = etree.SubElement(root, "from")
from_.text = "Chaitu"

# Create a child element <heading> and set its text content
heading = etree.SubElement(root, "heading")
heading.text = "Reminder"

# Create a child element <body> and set its text content
body = etree.SubElement(root, "body")
body.text = "Don't forget to meetup for lunch  at 12:30 pm tomorrow!"

# Create a nested child element <must_bring> under <body> and set its text content
must_bring = etree.SubElement(root, "must_bring")
must_bring.text = "Bring your Atm card"


# New element 1: <location> as sibling
location = etree.SubElement(root, "location")
location.text = "Cheese Cake Factory"

# New element 2: <agenda> as sibling
agenda = etree.SubElement(root, "agenda")
agenda.text = "Casual Meetup"

# Create an ElementTree object from the root element
tree = etree.ElementTree(root)

# Open the file for writing in binary mode and write the XML content to it
# The 'pretty_print=True' option formats the output nicely with indentation
# 'xml_declaration=True' adds the XML declaration (e.g., <?xml version='1.0'?>)
# 'encoding="UTF-8"' ensures the file is encoded in UTF-8
with open(sample_xml_output_file, "wb") as file:
    file.write(etree.tostring(tree, pretty_print=True, xml_declaration=True, encoding='UTF-8'))