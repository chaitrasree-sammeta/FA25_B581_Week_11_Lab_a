from lxml import etree  # Importing the lxml library's etree module for XML handling
from pathlib import Path  # Importing Path from pathlib to manage file paths

# Define the directory where the XML file will be saved
data_dir = Path.cwd() / 'data'

# Define the file path for the output XML file
sample_xml_output_file = data_dir / 'exercise_2.xml'

# Create the root element <patients>
patients = etree.Element("patients")

# Patient 003
patient_003 = etree.SubElement(patients, "patient", id="003")

first_name_003 = etree.SubElement(patient_003, "first_name")
first_name_003.text = "Alice"

last_name_003 = etree.SubElement(patient_003, "last_name")
last_name_003.text = "Johnson"

age_003 = etree.SubElement(patient_003, "age")
age_003.text = "29"

gender_003 = etree.SubElement(patient_003, "gender")
gender_003.text = "Female"

diagnosis_003 = etree.SubElement(patient_003, "diagnosis")
diagnosis_003.text = "Asthma"

medications_003 = etree.SubElement(patient_003, "medications")
med1_003 = etree.SubElement(medications_003, "medication")
med1_003.text = "Albuterol"
med2_003 = etree.SubElement(medications_003, "medication")
med2_003.text = "Montelukast"

# Patient 004
patient_004 = etree.SubElement(patients, "patient", id="004")

first_name_004 = etree.SubElement(patient_004, "first_name")
first_name_004.text = "Carlos"

last_name_004 = etree.SubElement(patient_004, "last_name")
last_name_004.text = "Ramirez"

age_004 = etree.SubElement(patient_004, "age")
age_004.text = "52"

gender_004 = etree.SubElement(patient_004, "gender")
gender_004.text = "Male"

diagnosis_004 = etree.SubElement(patient_004, "diagnosis")
diagnosis_004.text = "Hyperlipidemia"

medications_004 = etree.SubElement(patient_004, "medications")
med1_004 = etree.SubElement(medications_004, "medication")
med1_004.text = "Atorvastatin"
med2_004 = etree.SubElement(medications_004, "medication")
med2_004.text = "Ezetimibe"

# Create the XML tree
tree = etree.ElementTree(patients)

# Write to file (pretty-printed, with XML declaration)
with open(sample_xml_output_file, "wb") as file:
    file.write(etree.tostring(tree, pretty_print=True, xml_declaration=True, encoding='UTF-8'))




